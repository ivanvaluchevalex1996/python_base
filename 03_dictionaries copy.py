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
# 13. ЗАДАЧИ
# =============================================================================

# --- Задача: создать и заполнить словарь ---
# student = {}
# student["name"] = "Fedor"
# student["age"] = 20
# student["city"] = "Moscow"
# # {"name": "Fedor", "age": 20, "city": "Moscow"}


# --- Задача: безопасно получить значение ---
# prices = {"apple": 50, "banana": 30}
# apple_price = prices.get("apple", 0)    # 50
# grape_price = prices.get("grape", 0)    # 0


# --- Задача: подсчёт символов в строке ---
# text = "hello"
# counts = {}
# for char in text:
#     counts[char] = counts.get(char, 0) + 1
# # {"h": 1, "e": 1, "l": 2, "o": 1}
#
# или короче:
# from collections import Counter
# counts = Counter(text)


# --- Задача: dict comprehension — квадраты чисел ---
# nums = [1, 2, 3, 4]
# squares = {n: n ** 2 for n in nums}
# # {1: 1, 2: 4, 3: 9, 4: 16}


# --- Задача: объединить два словаря, второй приоритетнее ---
# defaults = {"theme": "light", "lang": "ru"}
# user_prefs = {"theme": "dark"}
# settings = defaults | user_prefs
# # {"theme": "dark", "lang": "ru"}


# --- Задача: инвертировать словарь (значения → ключи) ---
# original = {"a": 1, "b": 2, "c": 3}
# inverted = {v: k for k, v in original.items()}
# # {1: "a", 2: "b", 3: "c"}


# --- Задача: найти ключ по значению ---
# user = {"name": "Anna", "age": 25, "city": "Moscow"}
# target = "Moscow"
# key = next(k for k, v in user.items() if v == target)  # "city"


# --- Задача: отфильтровать словарь ---
# scores = {"math": 5, "eng": 3, "history": 4, "pe": 2}
# passed = {k: v for k, v in scores.items() if v >= 4}
# # {"math": 5, "history": 4}


# --- Задача: собрать словарь из двух списков через zip ---
# keys = ["apple", "banana", "grape"]
# prices = [50, 30, 80]
# prices_dict = dict(zip(keys, prices))
# # {"apple": 50, "banana": 30, "grape": 80}


# --- Задача: пройти два списка параллельно ---
# names = ["Anna", "Bob", "Kate"]
# ages = [25, 30, 22]
# for name, age in zip(names, ages):
#     print(f"{name}: {age}")


shop_stock = {"2358241350-50": 1, "2358000350-30": 24, "2358241350-00": 3}
shop_new_goods = {"2358241350-60": 10}

result = shop_stock | shop_new_goods


route = ("Moscow", "SPb")
# print(route)

students_courses = {}
name_age = frozenset(["Anatoly", 32])
students_courses[name_age] = ["Python", "C++"]  # ✅

# print(students_courses)


arr = [("A", 1), ("B", 2), ("C", 3)]
dict = {}
for key, value in arr:
    dict[key] = value   

print(dict)