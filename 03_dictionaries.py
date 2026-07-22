# 🔴🔴🔴 УРОК 3: СЛОВАРИ (dict)


# =============================================================================
# 1. ЧТО ТАКОЕ СЛОВАРЬ
# =============================================================================
#
# dict — коллекция пар «ключ → значение» (key-value).
# Ближайший аналог в JS — объект { } или Map.
#
# user = {
#     "name": "Anna",
#     "age": 25,
#     "city": "Moscow"
# }
#
# ключи уникальны, порядок вставки сохраняется (Python 3.7+)
# значения могут быть любого типа: число, строка, список, другой dict...


# =============================================================================
# 2. СОЗДАНИЕ СЛОВАРЯ
# =============================================================================
#
# пустой словарь:
# d = {}
# d = dict()
#
# с данными:
# user = {"name": "Anna", "age": 25}
# user = dict(name="Anna", age=25)       # только строковые ключи
# user = dict([("name", "Anna"), ("age", 25)])
# user = dict(zip(["name", "age"], ["Anna", 25]))   # см. раздел 8 (ZIP)
#
# dict.fromkeys(keys, value=None) — все ключи с одним значением:
# d = dict.fromkeys(["a", "b", "c"], 0)  # {"a": 0, "b": 0, "c": 0}
#
# ⚠️ { } — пустой dict
# ⚠️ set() — пустой set (не {} !)


# =============================================================================
# 3. ДОСТУП К ЗНАЧЕНИЯМ
# =============================================================================
#
# user = {"name": "Anna", "age": 25}
#
# user["name"]              # "Anna"        JS: user.name или user["name"]
# user["age"]               # 25
#
# user["email"]             # ❌ KeyError — ключа нет
#
# get() — безопасный доступ (ошибки нет):
# user.get("name")          # "Anna"
# user.get("email")         # None
# user.get("email", "—")    # "—" — значение по умолчанию
#                           # JS: user.email ?? "—"
#
# setdefault(key, default) — вернуть значение; если ключа нет — создать:
# user.setdefault("city", "Moscow")   # добавит city, если его не было
# user.setdefault("name", "Unknown")  # "Anna" — не перезапишет


# =============================================================================
# 4. ДОБАВЛЕНИЕ И ИЗМЕНЕНИЕ
# =============================================================================
#
# user = {"name": "Anna"}
#
# user["age"] = 25          # добавить новый ключ
# user["name"] = "Ann"      # изменить существующий
#
# update() — добавить/обновить несколько пар сразу:
# user.update({"city": "Moscow", "age": 26})
# user.update(city="SPb", job="dev")   # именованные аргументы
#                                       # JS: Object.assign(user, {...})
#
# объединение словарей (Python 3.9+):
# a = {"x": 1}
# b = {"y": 2}
# c = a | b                 # {"x": 1, "y": 2} — новый dict
# a |= b                    # изменить a на месте
#                           # JS: {...a, ...b}


# =============================================================================
# 5. УДАЛЕНИЕ
# =============================================================================
#
# user = {"name": "Anna", "age": 25, "city": "Moscow"}
#
# del user["city"]          # удалить по ключу. JS: delete user.city
# user.pop("age")           # удалить и вернуть значение (25)
# user.pop("x", None)       # если ключа нет — вернуть None (без ошибки)
# user.popitem()            # удалить и вернуть последнюю пару (key, value)
# user.clear()              # очистить словарь


# =============================================================================
# 6. ПРОВЕРКИ И СВОЙСТВА
# =============================================================================
#
# user = {"name": "Anna", "age": 25}
#
# "name" in user            # True   JS: "name" in user / user.hasOwnProperty("name")
# "email" in user           # False
# "Anna" in user            # False — ищется ключ, не значение!
#
# len(user)                 # 2      JS: Object.keys(user).length
# user.keys()               # dict_keys(["name", "age"])
# user.values()             # dict_values(["Anna", 25])
# user.items()              # dict_items([("name", "Anna"), ("age", 25)])
#
# list(user.keys())         # ["name", "age"]
# list(user.values())       # ["Anna", 25]
# list(user.items())        # [("name", "Anna"), ("age", 25)]


# =============================================================================
# 7. ЦИКЛЫ ПО СЛОВАРЮ
# =============================================================================
#
# user = {"name": "Anna", "age": 25, "city": "Moscow"}
#
# for key in user:                    # JS: for (const key in obj)
#     print(key, user[key])
#
# for key in user.keys():
#     print(key)
#
# for value in user.values():         # JS: Object.values(obj)
#     print(value)
#
# for key, value in user.items():     # JS: Object.entries(obj)
#     print(key, value)               #     for (const [key, value] of Object.entries(obj))
#
# enumerate для индекса:
# for i, (key, value) in enumerate(user.items()):
#     print(i, key, value)


# =============================================================================
# 8. ZIP — объединение последовательностей
# =============================================================================
#
# zip(a, b, ...) — склеивает элементы с одинаковым индексом в пары (кортежи).
# JS: встроенного zip нет; обычно arr1.map((x, i) => [x, arr2[i]])
#
# names = ["Anna", "Bob", "Kate"]
# ages = [25, 30, 22]
#
# zip(names, ages)              # <zip object ...> — итератор, не список!
# list(zip(names, ages))        # [("Anna", 25), ("Bob", 30), ("Kate", 22)]
#
# ⚠️ zip() возвращает итератор — «одноразовый»:
# z = zip(names, ages)
# list(z)   # [('Anna', 25), ('Bob', 30), ('Kate', 22)]
# list(z)   # [] — пусто, уже вычитали
#
# в цикле list() не нужен:
# for name, age in zip(names, ages):
#     print(name, age)
#
# создать словарь из двух списков (аналог Object.fromEntries + map):
# keys = ["one", "two", "three"]
# values = [1, 2, 3]
# my_dict = dict(zip(keys, values))   # {"one": 1, "two": 2, "three": 3}
#
# если списки разной длины — zip останавливается на коротком:
# list(zip([1, 2, 3], ["a", "b"]))  # [(1, "a"), (2, "b")]
#
# разобрать пары обратно (unzip):
# pairs = [("Anna", 25), ("Bob", 30)]
# names, ages = zip(*pairs)           # ("Anna", "Bob"), (25, 30)
#
# когда нужен list(zip(...)):
# — увидеть все пары в print
# — обратиться по индексу: pairs[0]
# — пройти по парам несколько раз
#
# когда list НЕ нужен:
# — for x, y in zip(a, b)
# — dict(zip(keys, values))


# =============================================================================
# 9. DICT COMPREHENSION (аналог Object.fromEntries + map/filter)
# =============================================================================
#
# JS: Object.fromEntries(nums.map(n => [n, n * 2]))
# squares = {n: n * 2 for n in [1, 2, 3]}     # {1: 2, 2: 4, 3: 6}
#
# JS: Object.fromEntries(Object.entries(obj).filter(...))
# evens = {k: v for k, v in d.items() if v % 2 == 0}
#
# инверсия (поменять ключи и значения местами):
# inverted = {v: k for k, v in user.items()}


# =============================================================================
# 10. КОПИИ И ВЛОЖЕННЫЕ СЛОВАРИ
# =============================================================================
#
# a = {"x": 1, "y": [1, 2]}
# b = a                     # та же ссылка! (как в JS)
# b = a.copy()              # shallow copy. JS: {...a}
# b = dict(a)               # то же
#
# import copy
# b = copy.deepcopy(a)      # deep copy — для вложенных dict/list
#
# вложенный словарь:
# student = {
#     "name": "Anna",
#     "grades": {"math": 5, "eng": 4}
# }
# student["grades"]["math"]           # 5
# student["grades"]["history"] = 3    # добавить предмет


# =============================================================================
# 11. КАКИЕ КЛЮЧИ МОЖНО ИСПОЛЬЗОВАТЬ
# =============================================================================
#
# ключ должен быть hashable (неизменяемым):
# ✅ str, int, float, bool, tuple (если внутри тоже hashable)
# ❌ list, dict, set — нельзя как ключ
#
# d = {("a", 1): "ok"}      # tuple как ключ — можно
# d = {[1, 2]: "no"}        # ❌ TypeError
#
# в JS ключи объекта всегда строки (или Symbol);
# в Python ключ — любой hashable тип:
# counts = {1: "one", True: "yes"}   # 1 и True — один ключ!


# =============================================================================
# 12. ЛОВУШКИ ДЛЯ ТЕХ, КТО ПРИШЁЛ С JS
# =============================================================================
#
# 1. user.name — только если ключ валидный идентификатор; обычно пишут user["name"]
# 2. "Anna" in user — проверяет КЛЮЧ, не значение
# 3. user["x"] — KeyError, если ключа нет; безопаснее user.get("x")
# 4. {} — dict, не set; пустой set: set()
# 5. = для dict — ссылка; копия: d.copy() или dict(d)
# 6. ключи 1 и True, 0 и False — считаются одним ключом
# 7. Object.keys(obj)     →  d.keys() или list(d)
# 8. Object.values(obj)   →  d.values()
# 9. Object.entries(obj)  →  d.items()
# 10. {...a, ...b}        →  a | b  или  {**a, **b} (старый способ)
# 11. zip(a, b) — итератор, не список; в for list() не нужен
# 12. JSON.parse/stringify — для dict используй import json:
#     json.dumps(d)  и  json.loads(s)


# =============================================================================
# 13. ЗАДАЧИ (без решений — пиши код ниже каждой задачи)
# =============================================================================


# -----------------------------------------------------------------------------
# Блок A: основы dict
# -----------------------------------------------------------------------------

# A1. Объедини два словаря магазина в один (новый dict, исходные не менять):
# shop_stock = {"2358241350-50": 1, "2358000350-30": 24, "2358241350-00": 3}
# shop_new_goods = {"2358241350-60": 10}
# all_data = shop_stock | shop_new_goods

# A2. Преобразуй список пар в словарь:
# arr = [("A", 1), ("B", 2), ("C", 3)]
# new_dict = {}
# for key, value in arr:
#     new_dict[key] = value
#     print(key)
#     print(value)

# new_dict = {k:v for k,v in  arr}


# A3. Создай словарь, где ключ — frozenset (имя + возраст), значение — список курсов:
students_courses = {}
name_age = frozenset(["Anatoly", 32])
# добавь курсы ["Python", "C++"] для этого студента
students_courses[name_age] = ["Python", "C++"]

# A4. Дан 
user = {"name": "Anna", "age": 25, "city": "Moscow"}
# Безопасно получи email; если ключа нет — верни "—"
save_key = user.get("email", "—")

# A5. Дан 
user = {"name": "Anna", "age": 25, "data" : "2"}
# Добавь city="Moscow" через setdefault (не перезаписывая name)
# user.setdefault("data", "1")

# A6. Дан 
user = {"name": "Anna", "age": 25, "city": "Moscow"}
# Удали city, затем age через pop; что вернёт pop("x", None)?
user.pop("name")


# -----------------------------------------------------------------------------
# Блок B: zip + dict
# -----------------------------------------------------------------------------

# B1. Даны 
keys = ["name", "age", "city"] 
values = ["Anna", 25, "Moscow"]
# Собери словарь user
user = dict(zip(keys, values))
# B2. Даны products = ["apple", "banana", "orange"] и prices = [50, 30, 45]
# Создай price_map: продукт → цена



# B3. Даны a = [1, 2, 3, 4] и b = ["x", "y"]
# Собери словарь из zip(a, b). Что получится и почему?

# B4. Дан 
pairs = [("a", 1), ("b", 2), ("c", 3)]
# Разбери на два кортежа keys и values через zip

# zipped = list(zip(*pairs))
k, v = list(zip(*pairs))

# B5. Даны 
names = ["Ivan", "Anna", "Petr"] 
# и
scores = [80, 95, 70]
# Создай result: имя → "pass" если score >= 80, иначе "fail"
# Используй zip + dict comprehension

result = {k:("pass" if v >=80 else "fail") for k,v in zip(names, scores)   }

# -----------------------------------------------------------------------------
# Блок C: dict comprehension
# -----------------------------------------------------------------------------

# C1.
nums = {1: 10, 2: 20, 3: 30, 4: 40}
# Новый словарь, где каждое значение умножено на 2
res = {k:v*2 for k,v in nums.items()}

# C2. 
user = {"name": "Anna", "age": 25, "city": "Moscow", "job": "dev"}
# Оставь только пары, где значение — строка
res = {k:v for k,v in user.items() if type(v) is str }

# C3. 
grades = {"math": 5, "eng": 3, "history": 4, "pe": 2}
# Оставь только предметы с оценкой >= 4
res = {k:v for k,v in grades.items() if v >=4}

# C4.
d = {"a": 1, "b": 2, "c": 3}
# Поменяй ключи и значения местами (инверсия)
res = {v:k for k,v in d.items()}

# C5. 
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Создай counts: слово → сколько раз встретилось
# Способ 1: цикл + setdefault
# Способ 2: dict comprehension (можно с set(words))

# new_dict = {}
# for w in words:
#     new_dict[w] = new_dict.get(w, 0) + 1

# for w in words:
#     new_dict.setdefault(w, 0) 
#     new_dict[w] += 1 
# 

# res = {w:words.count(w) for w in words}

# -----------------------------------------------------------------------------
# Блок D: бонус (часто на собесах)
# -----------------------------------------------------------------------------

# D1. 
ids = [101, 102, 103]
names = ["Anna", "Bob", "Kate"]
ages = [20, 22, 21]
# Собери список словарей:
# [{"id": 101, "name": "Anna", "age": 20}, {"id": 102, ...}, ...]
# Используй zip

res = [{"id": ids, "name": names, "age": ages} for ids,names,ages in  list(zip(ids, names, ages))]


# D2.
users = {
    "u1": {"name": "Anna", "age": 25},
    "u2": {"name": "Bob", "age": 30},
    "u3": {"name": "Kate", "age": 22},
}
# Создай словарь {id: name} — только id и имя

# dd = {}
# for user_id, info in users.items():
#     dd[user_id] = info["name"]

# for k in users:
#     dd[k] = users[k]["name"]


# D3.
products = [
    {"id": 1, "name": "apple", "price": 50},
    {"id": 2, "name": "banana", "price": 30},
    {"id": 3, "name": "orange", "price": 45},
]
# Создай словарь {id: price} — только id и цена
# Используй цикл или dict comprehension


# dd = {}
# for p in products:
#     dd[p["id"]] = p["price"]
#     print(p["id"])

dd = {p["id"]: p["price"] for p in products}


# D4.
orders = [
    {"user": "Anna", "item": "apple", "qty": 2},
    {"user": "Bob", "item": "banana", "qty": 1},
    {"user": "Anna", "item": "orange", "qty": 3},
]
# Создай словарь: имя пользователя → список купленных товаров
# {"Anna": ["apple", "orange"], "Bob": ["banana"]}
# Подсказка: setdefault или defaultdict

dd = {}
for x in orders:
    dd.setdefault(x["user"],[]).append(x["item"])


# -----------------------------------------------------------------------------
# Блок E: setdefault — группировка и подсчёт
# -----------------------------------------------------------------------------

# E1. Группировка чисел по чётности
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Создай словарь:
# {
#     "even": [2, 4, 6, 8, 10],
#     "odd": [1, 3, 5, 7, 9]
# }

dd = {}
for n in numbers:
    if n % 2 ==0:
        dd.setdefault("even", []).append(n)
    else:
        dd.setdefault("odd", []).append(n)
# print(dd)



# E2. Подсчёт количества букв в слове
word = "banana"
# Создай словарь: {'b': 1, 'a': 3, 'n': 2}
# Подсказка: используй setdefault для счётчика

dd = {}
for letter in word:
    dd[letter] = dd.setdefault(letter, 0) + 1



# E3. Группировка студентов по курсу
students_data = [
    {"name": "Alice", "course": "Python"},
    {"name": "Bob", "course": "JS"},
    {"name": "Charlie", "course": "Python"},
    {"name": "Diana", "course": "Java"},
    {"name": "Eve", "course": "JS"},
]
# Создай словарь: {название_курса: [имена_студентов]}
# {
#     "Python": ["Alice", "Charlie"],
#     "JS": ["Bob", "Eve"],
#     "Java": ["Diana"]
# }

dd = {}
for student in students_data:
    # неправильно
    # dd[student["course"]] = dd.setdefault(student["course"],[]).append(student["name"])
    # правильно
    dd.setdefault(student["course"],[]).append(student["name"])

# print(dd)


# E4. Группировка слов по первой букве
words = ["apple", "banana", "apricot", "blueberry", "cherry", "coconut"]
# Создай словарь: {буква: [слова_на_эту_букву]}
# {
#     "a": ["apple", "apricot"],
#     "b": ["banana", "blueberry"],
#     "c": ["cherry", "coconut"]
# }

dd = {}
for word in words:
    new_key = word[0:1]
    dd.setdefault(new_key,[]).append(word)


# E5. Подсчёт оценок студентов
grades = [
    {"student": "Anna", "grade": 5},
    {"student": "Bob", "grade": 4},
    {"student": "Anna", "grade": 3},
    {"student": "Bob", "grade": 5},
    {"student": "Charlie", "grade": 4},
]
# Создай словарь: {имя: [все_оценки]}
# {
#     "Anna": [5, 3],
#     "Bob": [4, 5],
#     "Charlie": [4]
# }

dd = {}
for item in grades:
    dd.setdefault(item["student"], []).append(item["grade"])

# print(dd)


# E6. Группировка товаров по категории
data = [
    {"category": "fruit", "item": "apple"},
    {"category": "fruit", "item": "banana"},
    {"category": "vegetable", "item": "carrot"},
    {"category": "fruit", "item": "orange"},
    {"category": "vegetable", "item": "potato"},
]
# Создай словарь: {категория: [список_товаров]}
# {
#     "fruit": ["apple", "banana", "orange"],
#     "vegetable": ["carrot", "potato"]
# }

dd = {}
for item in data:
    dd.setdefault(item["category"], []).append(item["item"])

# print(dd)


# E7. Сортировка чисел по диапазонам
numbers = [5, 12, 7, 25, 8, 30, 3, 15, 20]
# Создай словарь:
# {
#     "маленькие (0-10)": [5, 7, 8, 3],
#     "средние (11-20)": [12, 15, 20],
#     "большие (21+)": [25, 30]
# }

dd = {}
for n in numbers:
    if n < 11:
        key = "маленькие (0-10)"
    elif n < 21:
        key = "средние (11-20)"
    else:
        key = "большие (21+)"
    dd.setdefault(key, []).append(n)

    


# E8. Группировка по длине слова
words = ["cat", "dog", "elephant", "fox", "bear", "lion", "tiger", "ant"]
# Создай словарь: {длина_слова: [слова_такой_длины]}
# {
#     3: ["cat", "dog", "fox", "ant"],
#     5: ["bear", "lion"],
#     6: ["tiger"],
#     8: ["elephant"]
# }

dd = {}
for word in words:
    length = len(word)
    dd.setdefault(length,[]).append(word)

# print(dd)


# D5.
cities = ["Moscow", "SPb", "Kazan"]
populations = [12_000_000, 5_000_000, 1_200_000]
countries = ["RU", "RU", "RU"]
# Собери список словарей через zip:
# [{"city": "Moscow", "population": 12000000, "country": "RU"}, ...]

dd = [ {"city": c,"population": p,"country": co } for c, p, co in zip(cities, populations,countries )]


# D6.
inventory = {
    "apple": {"stock": 10, "price": 50},
    "banana": {"stock": 0, "price": 30},
    "orange": {"stock": 5, "price": 45},
}
# Создай словарь только тех товаров, где stock > 0
# Результат: {"apple": {"stock": 10, "price": 50}, "orange": {...}}

# new_data = {}

# for k,v in inventory.items():
#     if v["stock"] > 0:
#         new_data[k] = v

# new_data = {k:v for k,v in inventory.items() if v["stock"] > 0}

# D7.
students = {
    "s1": {"name": "Anna", "grades": {"math": 5, "eng": 4}},
    "s2": {"name": "Bob", "grades": {"math": 3, "eng": 5}},
    "s3": {"name": "Kate", "grades": {"math": 4, "eng": 4}},
}
# Создай словарь {id: средний балл}
# s1 → 4.5, s2 → 4.0, s3 → 4.0

# new_dict = {}

# for k,v in students.items():
#     print(v["grades"]["math"])
#     average = (v["grades"]["math"] + v["grades"]["eng"]) / 2
#     new_dict[k] = average


new_dict = {k:((v["grades"]["math"] + v["grades"]["eng"]) / 2) for k,v in students.items()}




# D8.
emails = ["anna@mail.com", "bob@mail.com", "kate@mail.com"]
domains = ["mail.com", "gmail.com", "mail.com"]
# Собери словарь {email: domain} через zip + dict comprehension
# {
#     "anna@mail.com": "mail.com",
#     "bob@mail.com": "gmail.com",
#     "kate@mail.com": "mail.com"
# }

# new_dict = {}
# for k,v in zip(emails,domains):
#     new_dict[k] = v

# new_dict = {k:v for k,v in zip(emails,domains)}



# D10.
pairs = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
# 1) Собери dict через dict(pairs) или dict comprehension

# new_dict = {}

# for k,v in pairs:
#     new_dict[k] = v

new_dict = {k:v for k,v in pairs}


# 2) Разбери обратно на keys и values через zip(*pairs)

k, v = zip(*pairs)

# 3) Снова собери dict из keys и values

new_dict_again = {k: v for k, v in zip(keys, values)}

# D10 - 2
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
# Распакуй на два кортежа: x_coords и y_coords

x_coords, y_coords = zip(*points)


# D11.
team = [
    {"name": "Anna", "role": "dev", "salary": 100000},
    {"name": "Bob", "role": "dev", "salary": 120000},
    {"name": "Kate", "role": "qa", "salary": 90000},
    {"name": "Ivan", "role": "qa", "salary": 95000},
]
# Сгруппируй по role:
# {"dev": ["Anna", "Bob"], "qa": ["Kate", "Ivan"]}

# new_dict = {}
# for item in team:
#     new_dict.setdefault(item["role"],[]).append(item["name"])



# D12.
old_users = {
    "u1": {"first": "Anna", "last": "Ivanova"},
    "u2": {"first": "Bob", "last": "Petrov"},
}
# Создай новый словарь:
# {"u1": "Anna Ivanova", "u2": "Bob Petrov"}
# через dict comprehension

new_dict = {}

for k,v in old_users.items():
    new_dict[k] = f"{v['first']} {v['last']}"


# =============================================================================
# 14. ЗАДАЧИ 2 — ещё на закрепление (без решений)
# =============================================================================


# -----------------------------------------------------------------------------
# Блок F1: основы dict
# -----------------------------------------------------------------------------

# F1-A1.
warehouse = {"sku-001": 15, "sku-002": 8, "sku-003": 0}
incoming = {"sku-003": 20, "sku-004": 5}
# Объедини в новый словарь. Исходные не менять.
# Если ключ есть в обоих — значение из incoming
new_dict = warehouse | incoming




# F1-A2.
pairs = [("red", 1), ("green", 2), ("blue", 3)]
# Преобразуй в словарь тремя способами:
# 1) цикл for
# 2) dict comprehension
# 3) dict(pairs)

# new_dict = {}
# for k,v in pairs:
#     new_dict[k] = v 

# new_dict = {k:v for k,v in pairs}

# new_dict = dict(pairs)



# F1-A5.
settings = {"theme": "dark", "lang": "ru"}
# Добавь "notifications": True через setdefault
# Попробуй setdefault("theme", "light") — theme не должен измениться
settings.setdefault("notifications", True)




# F1-A6.
# Удали "b" через del
cache = {"a": 1, "b": 2, "c": 3, "d": 4}

del cache["b"]
c_value = cache.pop("c")
# 3) Проверяем, что вернет pop("z", "missing")
result = cache.pop("z", "missing")


# -----------------------------------------------------------------------------
# Блок F2: zip + dict
# -----------------------------------------------------------------------------

# F2-B1.
fields = ["title", "author", "year"]
values = ["Dune", "Herbert", 1965]
# Собери словарь book

dd = dict(zip(fields, values))


# F2-B2.
currencies = ["USD", "EUR", "RUB"]
rates = [1.0, 0.92, 91.5]
# Словарь currency → rate
currency_rates = dict(zip(currencies, rates))



# F2-B4.
items = [("x", 100), ("y", 200), ("z", 300)]
# Разбери на keys и values через zip(*items)
# Снова собери dict из полученных keys и values

k,v = zip(*items)



# -----------------------------------------------------------------------------
# Блок F3: dict comprehension
# -----------------------------------------------------------------------------



# F3-C5.
log = ["login", "logout", "login", "error", "login", "logout", "error", "error"]
# Подсчитай события: событие → количество
# Способ 1: setdefault
# Способ 2: dict comprehension + count (или set(log))

# dd = {}
# for k in log:
#     dd[k] = dd.setdefault(k,0)+1

# dd = {k:log.count(k) for k in log}



# -----------------------------------------------------------------------------
# Блок F4: списки словарей, вложенные dict, zip
# -----------------------------------------------------------------------------

# F4-D1.
books = [
    {"id": 101, "title": "1984", "pages": 328},
    {"id": 102, "title": "Dune", "pages": 412},
    {"id": 103, "title": "Foundation", "pages": 255},
]
# Список словарей → {id: title}

dd = {}
for b in books:
    dd[b["id"]] = b["title"]

dd = {b["id"]: b["title"] for b in books}


# F4-D2.
transactions = [
    {"account": "A1", "amount": 100},
    {"account": "A2", "amount": 50},
    {"account": "A1", "amount": 200},
    {"account": "A3", "amount": 75},
    {"account": "A2", "amount": 25},
]
# Словарь: account → список всех amount
# setdefault

dd = {}
for t in transactions:
    dd.setdefault(t["account"], []).append(t["amount"]) 

transactions = [
    {"account": "A", "amount": 100},
    {"account": "B", "amount": 200},
    {"account": "A", "amount": 50},
    {"account": "C", "amount": 300},
    {"account": "B", "amount": 150},
]

# Полный пример для закрепления когда надо присваивать а когда нет и достаточно просто сделать setdefault (примитивы присваиваем, сложные - нет)

# 1. ГРУППИРОВКА по счетам (список сумм)
groups = {}
for t in transactions:
    groups.setdefault(t["account"], []).append(t["amount"])
# {'A': [100, 50], 'B': [200, 150], 'C': [300]}
# ✅ Работает! Список изменяется на месте

# 2. СЧЕТЧИК (количество транзакций по счетам)
counts = {}
for t in transactions:
    counts[t["account"]] = counts.get(t["account"], 0) + 1
# {'A': 2, 'B': 2, 'C': 1}
# ✅ Работает! Число заменяется новым

# 3. СУММА по счетам (тоже число → присваиваем!)
sums = {}
for t in transactions:
    sums[t["account"]] = sums.get(t["account"], 0) + t["amount"]
# {'A': 150, 'B': 350, 'C': 300}
# ✅ Работает! Число заменяется новым



# F4-D3.
codes = ["MSK", "SPB", "KZN"]
names = ["Moscow", "Saint Petersburg", "Kazan"]
regions = ["Central", "North-West", "Volga"]
# Список словарей через zip:
# [{"code": "MSK", "name": "Moscow", "region": "Central"}, ...]

dd = [{"code": c,"name":n, "region": r  } for c,n,r in zip(codes, names, regions)]

# F4-D4.
menu = {
    "pizza": {"price": 500, "available": True},
    "pasta": {"price": 350, "available": False},
    "salad": {"price": 250, "available": True},
    "soup": {"price": 200, "available": True},
}
# Только блюда, где available is True

dd = {}
for k,v in menu.items():
    if v["available"] == True:
        dd[k] =v




# F4-D6.
usernames = ["ivan", "anna", "petr"]
user_ids = [1001, 1002, 1003]
# {username: user_id} через zip + comprehension

dd = {k:v for k,v in zip(usernames, user_ids)}



# F4-D8.
employees = [
    {"dept": "sales", "name": "Oleg"},
    {"dept": "it", "name": "Nina"},
    {"dept": "sales", "name": "Pavel"},
    {"dept": "it", "name": "Kate"},
    {"dept": "hr", "name": "Ira"},
]
# Сгруппируй: dept → [имена]


# F4-D9.
contacts = {
    "c1": {"first": "Sergey", "last": "Volkov", "phone": "111"},
    "c2": {"first": "Elena", "last": "Morozova", "phone": "222"},
}
# {"c1": "Sergey Volkov (+111)", "c2": "Elena Morozova (+222)"}
# через dict comprehension

dd = {k:f"{v["first"]} {v["last"]} (+{v["phone"]})" for k,v in contacts.items()}


# -----------------------------------------------------------------------------
# Блок F5: setdefault — группировка и подсчёт
# -----------------------------------------------------------------------------

# F5-E1.
nums = [3, 7, 12, 18, 5, 9, 14, 21, 2, 16]
# Группировка:
# {"<10": [...], "10-19": [...], "20+": [...]}

dd = {}
for x in nums:
    if x < 10:
        dd.setdefault("<10", []).append(x)
    elif x < 20:
        dd.setdefault("10-19", []).append(x)
    else:
        dd.setdefault("20+", []).append(x)


# F5-E2.
text = "mississippi"
# Подсчёт букв: {'m': 1, 'i': 4, 's': 4, 'p': 2}

dd = {}
for x in text:
    dd[x] = dd.setdefault(x,0)+1



# F5-E4.
files = ["report.pdf", "image.png", "data.csv", "photo.png", "notes.txt", "chart.png"]
# Группировка по расширению (последняя часть после точки):
# {"pdf": ["report.pdf"], "png": [...], "csv": [...], "txt": [...]}

dd = {}
for x in files:
    _, last = x.split(".")
    dd.setdefault(last,[]).append(x)




# F5-E6.
products = [
    {"store": "A", "product": "milk"},
    {"store": "B", "product": "bread"},
    {"store": "A", "product": "eggs"},
    {"store": "C", "product": "milk"},
    {"store": "B", "product": "milk"},
]
# {store: [products]}

dd = {}
for x in products:
    dd.setdefault(x["store"], []).append(x["product"])



# F5-E8.
sentences = ["I am here", "You are there", "We are fine", "Go home now"]
# {длина_предложения_в_словах: [предложения]}

dd = {}
for s in sentences:
    dd.setdefault(len(s.split(" ")), []).append(s)


# -----------------------------------------------------------------------------
# Блок F6: смешанные (мини-проекты)
# -----------------------------------------------------------------------------

# F6-1.
# Дан список заказов. Верни итоговую корзину:
orders = [
    {"item": "apple", "qty": 2, "price": 50},
    {"item": "banana", "qty": 1, "price": 30},
    {"item": "apple", "qty": 3, "price": 50},
]
# 1) {item: общее_количество}  — setdefault 
# {'apple': 5, 'banana': 1}
# 2) {item: общая_сумма}       — qty * price, setdefault + суммирование
# {'apple': 250, 'banana': 30}

dd_count = {}
for x in orders:
    # dd_count[x["item"]] = dd_count.setdefault(x["item"], 0) + x["qty"]
    # или
    value = dd_count.get(x["item"], 0)
    dd_count[x["item"]] = value + x["qty"]
dd_sum = {}
for x in orders:
    total = x["qty"] * x["price"]  # ← Сначала считаем сумму заказа!
    value = dd_sum.get(x["item"], 0)
    dd_sum[x["item"]] = value + total  # ← Суммируем total



# F6-2.
# Объедини два прайс-листа; при конфликте бери меньшую цену:
shop_a = {"apple": 50, "banana": 30, "orange": 45}
shop_b = {"banana": 25, "orange": 50, "mango": 120}
# Результат: {"apple": 50, "banana": 25, "orange": 45, "mango": 120}

dd = {}
for k,v in shop_a.items():
    dd[k] = v

for k,v in shop_b.items():
    if k in dd:
        dd[k] = min(dd[k], v)
    else:
        dd[k] = v


print(shop_a.items())


# F6-3.
# Из списка пользователей собери:
users_raw = [
    {"id": 1, "name": "Anna", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Kate", "active": True},
    {"id": 4, "name": "Ivan", "active": True},
]
# active_map = {id: name} — только active=True
# inactive_count = сколько active=False

dd = {}
inactive_count=0
for x in users_raw:
    if x["active"] == True:
        dd[x["id"]] = x["name"]
    else:
        inactive_count+=1



# F6-4.
# Цепочка zip: pairs → dict → unzip → dict
raw = [("en", "hello"), ("ru", "привет"), ("de", "hallo")]
# 1) dict
dd = dict(raw)
# 2) keys, values через zip(*raw)
keys, values = zip(*raw)
# 3) снова dict из keys и values
dd = {k:v for k,v in zip(keys, values)}
# Проверь, что результат совпадает с шагом 1


# F6-5.
# Журнал просмотров: сгруппируй по пользователю и посчитай уникальные страницы.
views = [
    {"user": "anna", "page": "/home"},
    {"user": "bob", "page": "/catalog"},
    {"user": "anna", "page": "/cart"},
    {"user": "anna", "page": "/home"},
    {"user": "bob", "page": "/home"},
    {"user": "kate", "page": "/cart"},
]
# 1) dd = {user: [страницы]}  — через setdefault (дубликаты страниц оставить)
#    {'anna': ['/home', '/cart', '/home'], 'bob': ['/catalog', '/home'], 'kate': ['/cart']}
# 2) dd2 = {user: сколько_уникальных_страниц}
#    {'anna': 2, 'bob': 2, 'kate': 1}


dd = {}
dd2 = {}
for x in views:
    dd.setdefault(x["user"], []).append(x["page"])

for name, pages_list in dd.items():
    val = dd2.get(name,0)
    dd2[name] = val + len(set(pages_list))

print(dd)
print(dd2)


