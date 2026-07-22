# 🔴🔴🔴 УРОК 7a: LAMBDA (только лямбда)


# =============================================================================
# 1. ЧТО ТАКОЕ lambda
# =============================================================================
#
# lambda — короткая анонимная функция из ОДНОГО выражения.
# Ближайший аналог в JS — стрелочная функция с одним выражением:
#
# Python:  lambda x: x ** 2
# JS:         x =>   x ** 2
#
# ⚠️ lambda не заменяет def — это инструмент для коротких операций.


# =============================================================================
# 2. СИНТАКСИС
# =============================================================================
#
# lambda аргументы: выражение
#
# square = lambda x: x ** 2
# square(5)              # 25
#
# add = lambda a, b: a + b
# add(2, 3)              # 5
#
# greet = lambda: "hello"
# greet()                # "hello"
#
# full_name = lambda first, last: f"{first} {last}"
# full_name("Anna", "Ivanova")   # "Anna Ivanova"


# =============================================================================
# 3. ОГРАНИЧЕНИЯ lambda
# =============================================================================
#
# ✅ можно: одно выражение
# ❌ нельзя: несколько строк, if/else блок, цикл, присваивание
#
# lambda x: x * 2                    # ✅
# lambda x: x * 2 if x > 0 else 0    # ✅ тернарник — это выражение
#
# lambda x:                        # ❌
#     print(x)
#     return x * 2
#
# для сложной логики → def


# =============================================================================
# 4. sorted() + key=lambda
# =============================================================================
#
# users = [("Anna", 25), ("Bob", 30), ("Kate", 20)]
# sorted(users, key=lambda x: x[1])
# # [('Kate', 20), ('Anna', 25), ('Bob', 30)]
#
# sorted(users, key=lambda x: x[1], reverse=True)
# # по убыванию возраста
#
# words = ["banana", "pie", "Washington"]
# sorted(words, key=lambda w: len(w))
# # по длине слова
#
# JS:
# users.sort((a, b) => a[1] - b[1])


# =============================================================================
# 5. filter() + lambda
# =============================================================================
#
# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# # [2, 4, 6]
#
# JS:
# nums.filter(x => x % 2 === 0)


# =============================================================================
# 6. map() + lambda
# =============================================================================
#
# nums = [1, 2, 3, 4]
# squares = list(map(lambda x: x ** 2, nums))
# # [1, 4, 9, 16]
#
# JS:
# nums.map(x => x ** 2)


# =============================================================================
# 7. ТЕРНАРНИК ВНУТРИ lambda
# =============================================================================
#
# numbers = [1, 2, 3, 4, 5]
# labels = list(map(lambda n: "even" if n % 2 == 0 else "odd", numbers))
# # ['odd', 'even', 'odd', 'even', 'odd']
#
# JS:
# numbers.map(n => n % 2 === 0 ? "even" : "odd")


# =============================================================================
# 8. lambda vs def — КОГДА ЧТО
# =============================================================================
#
# lambda — когда:
# - короткая операция для key= / filter / map
# - функция нужна «на один раз»
# - одно выражение
#
# def — когда:
# - несколько строк логики
# - нужен docstring
# - функция переиспользуется и должна иметь имя
# - сложные условия и циклы


# =============================================================================
# 9. ЛОВУШКИ ДЛЯ ТЕХ, КТО ПРИШЁЛ С JS
# =============================================================================
#
# 1. const f = x => x * 2     →  f = lambda x: x * 2
# 2. lambda без скобок у аргументов: lambda a, b: a + b
# 3. нет return — результат выражения возвращается автоматически
# 4. sorted/filter/map возвращают итератор → часто нужен list()
# 5. lambda в цикле с замыканием — классическая ловушка (продвинутое)


# =============================================================================
# 10. ПРИМЕРЫ (твои решения)
# =============================================================================

double = lambda x: x * x
add = lambda a, b: a + b
greet = lambda: "hello"
# full_name = lambda first, last: f"{first} {last}"


# =============================================================================
# 11. ЗАДАЧИ — только lambda (без решений)
# =============================================================================


# L1. Создай lambda square — возвращает квадрат числа
# Проверь: square(6) → 36


square = lambda a: a*a


# L2. Создай lambda is_positive — True если число > 0

is_positive = lambda a: a > 0

# L3.
nums = [1, -2, 3, -4, 5, 0]
# Через filter + lambda получи только положительные числа

dd = list(filter(lambda x: x>0, nums))

dd = [x for x in nums if x > 0]

# L4.
nums = [1, 2, 3, 4, 5]
# Через map + lambda получи кубы чисел: [1, 8, 27, 64, 125]

dd = list(map(lambda x: x*x*x, nums))

dd = [x*x*x for x in nums]

# L5.
words = ["python", "js", "go", "rust"]
# Отсортируй по длине слова через sorted(..., key=lambda ...)

dd = sorted(words, key=lambda x: len(x))


# L6.
pairs = [("Anna", 25), ("Bob", 30), ("Kate", 20), ("Ivan", 35)]
# Отсортируй по возрасту (2-й элемент) по убыванию

dd = sorted(pairs, key=lambda x:x[1], reverse=True)


# L7.
nums = [10, 15, 20, 25, 30, 35]
# Через filter + lambda оставь только числа, кратные 5

dd = list(filter(lambda x: x%5 ==0, nums))

# L8.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Через map + lambda получи метки: "even" / "odd"

dd = list(map(lambda x: "even" if x % 2 ==0 else "odd" , nums))

dd = ["even" if x % 2 ==0 else "odd" for x in nums]

# const arr = nums.map(el=> el % 2 === 0 ? "even" : "odd")


# L9.
prices = [100, 250, 80, 500, 120]
# Через map + lambda примени скидку 10%: price * 0.9

# dd = [x*0.9 for x in  prices]
dd = list(map(lambda x: x*0.9 ,prices))


func = lambda x: x*0.9
# print(func(prices))  // "лямбда ожидает число, а не список".

dd = list(map(func,prices))

# const func1 = (x)=> x*0.9

# const arr = prices.map(func1)


# L10.
students = [
    ("Anna", 85),
    ("Bob", 92),
    ("Kate", 78),
    ("Ivan", 95),
]
# Отсортируй по оценке по убыванию
# Через filter оставь только с оценкой >= 90

sorted_data = sorted(students, key=lambda x:x[1], reverse=True)
new_students = [k for k,v in students if v >=90 ]
# new_students = list(filter(lambda x:x[1]>=90,students))



# L11.
data = ["", "hello", "", "world", "py", ""]
# Через filter убери пустые строки

dd = list(filter(lambda x: x!="", data))
dd = [x for x in data if x != ""]


# L12.
strings = ["abc", "de", "fghi", "jk"]
# Отсортируй по длине, при равной длине — по алфавиту
# Подсказка: key=lambda s: (len(s), s)

dd = sorted(strings, key=lambda x: len(x))


# L13.
nums = [-3, -1, 0, 2, 5]
# Через map + lambda получи абсолютные значения

# dd = list(map(lambda x: abs(x)))
# или
# dd = list(map(abs))


# L14.
words = ["Apple", "banana", "Cherry", "date"]
# Через sorted + lambda отсортируй без учёта регистра
# Подсказка: key=lambda w: w.lower()

dd = sorted(words, key=lambda x: x.lower())


# L15.
pairs = [(1, 3), (2, 1), (5, 2), (4, 4)]
# Отсортируй по сумме элементов кортежа
# Подсказка: key=lambda x: x[0] + x[1]

dd = sorted(pairs, key=lambda x: x[0] + x[1])

students = [
    ("Alice", 25, "A"),
    ("Bob", 22, "B"),
    ("Charlie", 25, "A"),
    ("Diana", 22, "A"),
]
# Отсортируй по возрасту (по возрастанию), а при равном возрасте — по имени (по алфавиту)
# Ожидаемый результат: [('Bob', 22, 'B'), ('Diana', 22, 'A'), ('Alice', 25, 'A'), ('Charlie', 25, 'A')]

dd = sorted(students, key=lambda x: (x[1], x[0]))

products = [
    {"name": "Laptop", "price": 1000, "rating": 4.5},
    {"name": "Phone", "price": 800, "rating": 4.8},
    {"name": "Tablet", "price": 1000, "rating": 4.2},
    {"name": "Monitor", "price": 300, "rating": 4.5},
]

# ============ ВАРИАНТ 1: ЧЕРЕЗ ОТРИЦАНИЕ (ТОЛЬКО ДЛЯ ЧИСЕЛ) ============
dd1 = sorted(products, key=lambda x: (-x["price"], -x["rating"]))
print("Вариант 1 (отрицание):", dd1)

# ============ ВАРИАНТ 2: ЧЕРЕЗ REVERSE (УНИВЕРСАЛЬНЫЙ) ============
# Подходит для любых типов данных: строк, дат, кортежей и т.д.
dd2 = sorted(products, key=lambda x: (x["price"], x["rating"]), reverse=True)
print("Вариант 2 (reverse):", dd2)

# ============ ПОЧЕМУ reverse УНИВЕРСАЛЬНЕЕ? ============
# Пример с сортировкой по строковому полю (имя по убыванию):
products_with_names = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 1000},
]

# ❌ Отрицание НЕ РАБОТАЕТ со строками!
# sorted(products_with_names, key=lambda x: (-x["name"], -x["price"]))
# TypeError: bad operand type for unary -: 'str'

# ✅ reverse РАБОТАЕТ с любыми типами!
sorted(products_with_names, key=lambda x: (x["name"], x["price"]), reverse=True)
# [{'name': 'Tablet', 'price': 1000}, {'name': 'Phone', 'price': 800}, {'name': 'Laptop', 'price': 1000}]

# ============ КОГДА ИСПОЛЬЗОВАТЬ КАЖДЫЙ ВАРИАНТ ============
"""
Отрицание (-):
  ✅ Работает только с числами (int, float)
  ✅ Компактно и быстро
  ❌ Не работает со строками, датами, булевыми значениями
  📌 Использовать: когда сортируем ТОЛЬКО по числовым полям

reverse=True:
  ✅ Работает с ЛЮБЫМИ типами данных
  ✅ Универсально и читаемо
  ❌ Немного медленнее (но разница незаметна)
  📌 Использовать: когда есть строки или смешанные типы
"""

# ============ СМЕШАННЫЙ ПРИМЕР: ЦЕНА (число) + ИМЯ (строка) ============
# ❌ Неправильно (отрицание не работает со строками)
# sorted(products_with_names, key=lambda x: (-x["price"], -x["name"]))

# ✅ Правильно (используем reverse)
sorted(products_with_names, key=lambda x: (x["price"], x["name"]), reverse=True)
# Сначала по цене (убывание), потом по имени (убывание)

# ============ ЕСЛИ НУЖНА СМЕШАННАЯ СОРТИРОВКА ============
# Пример: цена по убыванию, имя по возрастанию
sorted(products_with_names, key=lambda x: (-x["price"], x["name"]))
# Здесь отрицание только для числа, имя сортируется обычным способом



words = ["cat", "elephant", "dog", "giraffe", "bird", "hippopotamus"]

dd = list(filter(lambda x: len(x)>=3 and len(x)<=8, words))

dd = [x for x in words if len(x) >3 and len(x) < 9]
