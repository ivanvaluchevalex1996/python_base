# 🔴🔴🔴 УРОК 9: Pandas для ML-инженера
#
# Зачем Pandas в ML:
# - данные часто приходят как CSV / Excel / таблица из БД
# - удобно смотреть, чистить, фильтровать, группировать
# - потом отдать числа в модель: .to_numpy() / sklearn
#
# Цепочка:
#   CSV → pandas (EDA + cleaning) → NumPy / sklearn / torch (модель)
#
# NumPy  = матрицы чисел
# Pandas = таблица со столбцами (имена, разные типы, NaN)


import pandas as pd
import numpy as np


# =============================================================================
# 1. Series и DataFrame
# =============================================================================
#
# Series     — один столбец (1D) с индексом
# DataFrame  — таблица (2D): строки + именованные столбцы
#
# В работе 95% времени работаешь с DataFrame.

s = pd.Series([10, 20, 30], name="age")
print("Series:\n", s)

df = pd.DataFrame({
    "name": ["Anna", "Bob", "Kate", "Dan", "Eva"],
    "age": [25, 30, 22, 35, 28],
    "city": ["Moscow", "SPb", "Moscow", "Kazan", "SPb"],
    "salary": [80, 120, 70, 150, 95],
    "bought": [1, 0, 1, 1, 0],   # целевая переменная y (пример)
})
print("\nDataFrame:\n", df)


# =============================================================================
# 2. ПЕРВЫЙ ВЗГЛЯД НА ДАННЫЕ (EDA) — делают ВСЕГДА
# =============================================================================
#
# В реале чаще:
#   df = pd.read_csv("data.csv")
#   df = pd.read_excel("data.xlsx")

print("\n--- EDA ---")
print(df.head())              # первые 5 строк
print("shape:", df.shape)     # (строки, столбцы)
print("columns:", df.columns.tolist())
print(df.dtypes)              # типы столбцов
print(df.describe())          # статистика по числам
# print(df.info())            # типы + сколько non-null (в консоли длинно)


# =============================================================================
# 3. ВЫБОР СТОЛБЦОВ
# =============================================================================

print("\n--- столбцы ---")
print(df["age"])                    # один столбец → Series
print(df[["name", "salary"]])       # несколько → DataFrame

# Для модели обычно так:
features = ["age", "salary"]
X_df = df[features]
y = df["bought"]
print("X:\n", X_df)
print("y:\n", y)


# =============================================================================
# 4. ФИЛЬТРАЦИЯ СТРОК
# =============================================================================

print("\n--- фильтр ---")
print(df[df["age"] > 25])
print(df[df["city"] == "Moscow"])
print(df[(df["age"] > 25) & (df["salary"] >= 100)])  # AND
print(df[(df["city"] == "Moscow") | (df["city"] == "SPb")])  # OR

# isin — удобнее списка городов
print(df[df["city"].isin(["Moscow", "Kazan"])])


# =============================================================================
# 5. loc / iloc — доступ по метке и по позиции
# =============================================================================
#
# loc  — по именам (index / columns)
# iloc — по номерам (как в списках)

print("\n--- loc / iloc ---")
print(df.loc[0, "name"])          # Anna
print(df.loc[0:2, ["name", "age"]])
print(df.iloc[0, 0])              # Anna (строка 0, столбец 0)
print(df.iloc[:3, :2])            # первые 3 строки, первые 2 столбца


# =============================================================================
# 6. НОВЫЕ СТОЛБЦЫ
# =============================================================================

print("\n--- новые столбцы ---")
df["salary_k"] = df["salary"] / 100
df["is_moscow"] = (df["city"] == "Moscow").astype(int)
print(df[["name", "salary", "salary_k", "is_moscow"]])


# =============================================================================
# 7. ПРОПУСКИ (NaN) — в реальных данных почти всегда есть
# =============================================================================

print("\n--- NaN ---")
df_nan = df.copy()
df_nan.loc[1, "salary"] = np.nan
df_nan.loc[3, "age"] = np.nan
print(df_nan)

print("сколько пропусков:\n", df_nan.isna().sum())

# Варианты:
print(df_nan.dropna())                         # удалить строки с NaN
print(df_nan.fillna({"age": df_nan["age"].median(),
                     "salary": df_nan["salary"].median()}))  # заполнить


# =============================================================================
# 8. value_counts / sort — быстрая аналитика
# =============================================================================

print("\n--- value_counts / sort ---")
print(df["city"].value_counts())
print(df.sort_values("salary", ascending=False))


# =============================================================================
# 9. groupby — агрегации (очень частый инструмент)
# =============================================================================
#
# «средняя зарплата по городу», «сколько покупок по сегменту»

print("\n--- groupby ---")
print(df.groupby("city")["salary"].mean())
print(df.groupby("city").agg(
    avg_salary=("salary", "mean"),
    avg_age=("age", "mean"),
    count=("name", "count"),
))


# =============================================================================
# 10. merge — склеить две таблицы (как JOIN в SQL)
# =============================================================================

print("\n--- merge ---")
users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Anna", "Bob", "Kate"],
})
orders = pd.DataFrame({
    "user_id": [1, 1, 2],
    "amount": [100, 50, 200],
})
print(users.merge(orders, on="user_id", how="left"))
# how: inner / left / right / outer


# =============================================================================
# 11. КАТЕГОРИИ → ЧИСЛА (перед моделью)
# =============================================================================
#
# Модель не ест строки "Moscow". Нужны числа.

print("\n--- encoding ---")

# One-hot: каждый город → свой столбец 0/1
city_oh = pd.get_dummies(df["city"], prefix="city")
print(city_oh)

# Label encoding (простой вариант через factorize)
df["city_id"], city_names = pd.factorize(df["city"])
print(df[["city", "city_id"]])
print("города:", list(city_names))


# =============================================================================
# 12. ИЗ PANDAS В NUMPY / МОДЕЛЬ
# =============================================================================

print("\n--- to ML ---")
feature_cols = ["age", "salary", "is_moscow"]
X = df[feature_cols].to_numpy(dtype=float)
y = df["bought"].to_numpy()
print("X shape:", X.shape, "\n", X)
print("y shape:", y.shape, "\n", y)

# Обратно (редко нужно):
# pd.DataFrame(X, columns=feature_cols)


# =============================================================================
# 13. ТИПИЧНЫЙ ML-ПАЙПЛАЙН НА PANDAS (минимум)
# =============================================================================

print("\n--- pipeline sketch ---")
data = pd.DataFrame({
    "age": [25, 30, np.nan, 35, 28, 40],
    "city": ["Moscow", "SPb", "Moscow", "Kazan", "SPb", "Moscow"],
    "salary": [80, 120, 70, np.nan, 95, 110],
    "bought": [1, 0, 1, 1, 0, 1],
})

# 1) посмотреть
print(data.head())
print(data.isna().sum())

# 2) заполнить пропуски
data["age"] = data["age"].fillna(data["age"].median())
data["salary"] = data["salary"].fillna(data["salary"].median())

# 3) закодировать категории
data = pd.get_dummies(data, columns=["city"], drop_first=True)

# 4) разделить X / y
y = data["bought"].to_numpy()
X = data.drop(columns=["bought"]).to_numpy(dtype=float)
print("X:", X.shape, "y:", y.shape)
print(data)


# =============================================================================
# 14. ЧТО УЧИТЬ ДАЛЬШЕ (чеклист ML-инженера)
# =============================================================================
#
# ✅ ОБЯЗАТЕЛЬНО:
# 1. read_csv / head / shape / dtypes / describe
# 2. выбор столбцов df["col"], df[["a", "b"]]
# 3. фильтры df[условие]
# 4. loc / iloc
# 5. NaN: isna / fillna / dropna
# 6. groupby + agg
# 7. sort_values / value_counts
# 8. get_dummies (one-hot)
# 9. to_numpy() → в модель
# 10. merge (join таблиц)
#
# ⬜ ПОЛЕЗНО:
# - apply (осторожно, медленнее векторизации)
# - pivot_table
# - работа с датами: pd.to_datetime
# - astype / rename / drop
#
# ⬜ РЯДОМ ПО СТЕКУ:
# - sklearn: train_test_split, Pipeline, ColumnTransformer
# - NumPy: уже знаешь из урока 8
# - seaborn/matplotlib: графики по df
#
# Правило:
# pandas  → таблица: почистить, понять, подготовить
# NumPy   → матрица чисел для вычислений/модели


# =============================================================================
# 15. МИНИ-ПРАКТИКА (раскомментируй и реши)
# =============================================================================
#
# 1) Создай DataFrame с колонками: name, age, score, passed (0/1)
# 2) Выведи тех, у кого score >= 70
# 3) Посчитай средний score
# 4) Добавь столбец grade: "A" если score >= 90 иначе "B"
# 5) Сделай X из ["age", "score"] и y из passed через .to_numpy()
#
# practice = pd.DataFrame({...})
# ...
