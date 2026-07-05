# 🔴🔴🔴 УРОК 6: ЦИКЛЫ И LIST COMPREHENSION


# =============================================================================
# 1. ЗАЧЕМ НУЖНЫ ЦИКЛЫ
# =============================================================================
#
# Цикл — повторение одного и того же действия несколько раз.
# Вместо copy-paste кода 100 раз — одна конструкция с циклом.
#
# print(0)
# print(1)
# print(2)
# ...
#
# for i in range(3):
#     print(i)   # 0, 1, 2


# =============================================================================
# 2. ЦИКЛ FOR — ПЕРЕБОР ПОСЛЕДОВАТЕЛЬНОСТИ
# =============================================================================
#
# for элемент in последовательность:
#     код
#
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# # apple
# # banana
# # cherry
#
# JS: for (const fruit of fruits) { console.log(fruit); }


# =============================================================================
# 3. RANGE — ЦИКЛ ПО ЧИСЛАМ
# =============================================================================
#
# range(stop)              — от 0 до stop-1
# range(start, stop)       — от start до stop-1
# range(start, stop, step) — с шагом step
#
# list(range(5))           # [0, 1, 2, 3, 4]
# list(range(1, 4))        # [1, 2, 3]
# list(range(0, 11, 2))    # [0, 2, 4, 6, 8, 10]
# list(range(5, 0, -1))    # [5, 4, 3, 2, 1]
#
# stop НЕ включается (как в срезах)!
# до 100 включительно: range(a, 101)
#
# for i in range(3):
#     print(i)             # 0, 1, 2
#
# JS: for (let i = 0; i < 3; i++) { console.log(i); }


# =============================================================================
# 4. FOR + RANGE(LEN(...)) — ЦИКЛ ПО ИНДЕКСАМ
# =============================================================================
#
# когда нужен индекс, а не только значение:
#
# nums = [10, 20, 30]
# for i in range(len(nums)):
#     print(i, nums[i])
# # 0 10
# # 1 20
# # 2 30
#
# JS: for (let i = 0; i < nums.length; i++) { ... }


# =============================================================================
# 5. ENUMERATE — ИНДЕКС И ЗНАЧЕНИЕ СРАЗУ
# =============================================================================
#
# удобнее, чем range(len(...)):
#
# fruits = ["apple", "banana", "cherry"]
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
# # 0 apple
# # 1 banana
# # 2 cherry
# print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
#
# enumerate(fruits, start=1)   # индекс с 1, а не с 0
#
# JS: fruits.forEach((fruit, i) => console.log(i, fruit));


# =============================================================================
# 6. ЦИКЛ ПО СТРОКЕ
# =============================================================================
#
# строка — последовательность символов, for идёт посимвольно:
#
# word = "Python"
# for char in word:
#     print(char)
# # P y t h o n (каждый на новой строке)
#
# JS: for (const char of "Python") { ... }


# =============================================================================
# 7. ЦИКЛ ПО СЛОВАРЮ
# =============================================================================
#
# dict_age = {"Антон": 20, "Борис": 25, "Виктор": 15}
#
# только ключи (по умолчанию):
# for name in dict_age:
#     print(name)
#
# ключ + значение:
# for name, age in dict_age.items():
#     print(name, age)
#
# только значения:
# for age in dict_age.values():
#     print(age)
#
# JS:
# Object.keys(obj)    →  for name in dict_age
# Object.entries(obj) →  for name, age in dict_age.items()
# Object.values(obj)  →  for age in dict_age.values()


# =============================================================================
# 8. ЦИКЛ WHILE — ПОКА УСЛОВИЕ True
# =============================================================================
#
# while условие:
#     код
#
# счётчик = 0
# while счётчик < 3:
#     print(счётчик)
#     счётчик += 1
# # 0, 1, 2
#
# ⚠️ если условие всегда True — бесконечный цикл!
# обязательно меняй переменную внутри цикла.
#
# JS:
# let count = 0;
# while (count < 3) {
#     console.log(count);
#     count++;
# }


# =============================================================================
# 9. BREAK — ВЫЙТИ ИЗ ЦИКЛА
# =============================================================================
#
# прерывает цикл досрочно:
#
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# # 0, 1, 2, 3, 4  (на 5 остановился)
#
# JS: break — то же самое


# =============================================================================
# 10. CONTINUE — ПРОПУСТИТЬ ИТЕРАЦИЮ
# =============================================================================
#
# переходит к следующей итерации, не выполняя остаток тела цикла:
#
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# # 0, 1, 3, 4  (2 пропущен)
#
# JS: continue — то же самое


# =============================================================================
# 11. ELSE У ЦИКЛА
# =============================================================================
#
# else после for/while выполнится, если цикл завершился БЕЗ break:
#
# for i in range(3):
#     print(i)
# else:
#     print("Готово!")
# # 0, 1, 2, Готово!
#
# for i in range(3):
#     if i == 1:
#         break
# else:
#     print("Готово!")   # не выведется — был break
#
# в JS аналога нет.


# =============================================================================
# 12. ВЛОЖЕННЫЕ ЦИКЛЫ
# =============================================================================
#
# цикл внутри цикла — для таблиц, матриц, комбинаций:
#
# for i in range(3):
#     for j in range(2):
#         print(i, j)
# # 0 0, 0 1, 1 0, 1 1, 2 0, 2 1
#
# таблица умножения:
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i * j, end=" ")
#     print()   # новая строка после каждого i


# =============================================================================
# 13. НАКОПЛЕНИЕ РЕЗУЛЬТАТА В ЦИКЛЕ
# =============================================================================
#
# частый паттерн — сумма, счётчик, список:
#
# nums = [1, 2, 3, 4, 5]
#
# total = 0
# for n in nums:
#     total += n
# # total = 15
#
# count = 0
# for n in nums:
#     if n % 2 == 0:
#         count += 1
# # count = 2
#
# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)
# # evens = [2, 4]
#
# тот же паттерн «for + append» короче через list comprehension — см. раздел 15.
#
# JS: arr.reduce((sum, n) => sum + n, 0)


# =============================================================================
# 14. FOR VS WHILE — КОГДА ЧТО
# =============================================================================
#
# for — когда знаешь, сколько раз повторить (список, range, строка)
# while — когда повторять, пока условие True (не знаешь заранее число итераций)
#
# for i in range(10):        # 10 раз — for
#     ...
#
# while user_input != "exit":   # пока не выйдет — while
#     user_input = input("Команда: ")


# =============================================================================
# 15. LIST COMPREHENSION — ЗАЧЕМ
# =============================================================================
#
# List comprehension — короткий способ создать новый список из другой последовательности.
# Вместо цикла for + append — одна строка.
#
# nums = [1, 2, 3, 4, 5]
#
# через цикл:
# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)
# # evens = [2, 4]
#
# через comprehension:
# evens = [n for n in nums if n % 2 == 0]
# # evens = [2, 4]
#
# JS-аналоги:
# arr.map(x => ...)     →  [выражение for x in arr]
# arr.filter(x => ...)  →  [x for x in arr if условие]


# =============================================================================
# 16. БАЗОВЫЙ СИНТАКСИС COMPREHENSION
# =============================================================================
#
# [выражение for элемент in последовательность]
#
# doubled = [n * 2 for n in [1, 2, 3]]       # [2, 4, 6]
# squares = [n ** 2 for n in range(1, 6)]    # [1, 4, 9, 16, 25]
#
# JS: [1, 2, 3].map(n => n * 2)
#
# выражение слева — что попадёт в новый список.
# for n in ... — откуда берём элементы (список, range, строка и т.д.)


# =============================================================================
# 17. COMPREHENSION С УСЛОВИЕМ (FILTER)
# =============================================================================
#
# [выражение for элемент in последовательность if условие]
#
# evens = [n for n in [1, 2, 3, 4] if n % 2 == 0]   # [2, 4]
# big = [n for n in nums if n > 10]                 # только > 10
#
# JS: nums.filter(n => n % 2 === 0)
#
# if в конце — фильтр: элемент попадёт в список только если условие True.


# =============================================================================
# 18. MAP + FILTER ВМЕСТЕ
# =============================================================================
#
# сначала фильтр (if), потом выражение применяется к отфильтрованным:
#
# nums = [1, 2, 3, 4, 5, 6]
# result = [n * 2 for n in nums if n % 2 == 0]
# # [4, 8, 12]  — чётные, умноженные на 2
#
# JS: nums.filter(n => n % 2 === 0).map(n => n * 2)
#
# words = ["hi", "hello", "hey", "bye"]
# long_upper = [w.upper() for w in words if len(w) > 3]
# # ["HELLO"]
#
# сумма чисел, делящихся на 3 или 5:
# a, b = 1, 10
# result = sum([x for x in range(a, b + 1) if x % 3 == 0 or x % 5 == 0])
# # 33


# =============================================================================
# 19. COMPREHENSION С RANGE, СТРОКАМИ, ENUMERATE
# =============================================================================
#
# list(range(...)) часто заменяется comprehension:
#
# nums = [n for n in range(10)]           # [0, 1, 2, ..., 9]
# odds = [n for n in range(1, 20) if n % 2 != 0]
# squares = [n ** 2 for n in range(1, 6)]  # [1, 4, 9, 16, 25]
#
# сумма квадратов чётных от 1 до 10:
# total = sum([n ** 2 for n in range(1, 11) if n % 2 == 0])
# # 4 + 16 + 36 + 64 + 100 = 220
#
# строка — последовательность символов:
# word = "Python"
# chars = [c for c in word]              # ["P", "y", "t", "h", "o", "n"]
# vowels = [c for c in word if c in "aeiouAEIOU"]
#
# words = ["apple", "banana", "cherry"]
# lengths = [len(w) for w in words]        # [5, 6, 6]
# upper_words = [w.upper() for w in words]
#
# pairs = [(i, x) for i, x in enumerate(["a", "b", "c"])]
# # [(0, "a"), (1, "b"), (2, "c")]
#
# indexed = [f"{i}: {name}" for i, name in enumerate(names, start=1)]
#
# JS: arr.map((x, i) => `${i}: ${x}`)


# =============================================================================
# 20. IF / ELSE В ВЫРАЖЕНИИ (НЕ ФИЛЬТР!)
# =============================================================================
#
# if в НАЧАЛЕ (перед for) — это тернарный оператор в выражении:
#
# nums = [1, 2, 3, 4]
# labels = ["even" if n % 2 == 0 else "odd" for n in nums]
# # ["odd", "even", "odd", "even"]
#
# abs_vals = [n if n >= 0 else -n for n in [-3, 5, -1, 0]]
# # [3, 5, 1, 0]
#
# JS: nums.map(n => n % 2 === 0 ? "even" : "odd")
#
# ⚠️ не путай:
# [x for x in arr if x > 0]              — фильтр (только положительные)
# ["pos" if x > 0 else "neg" for x in arr]  — все элементы, но с преобразованием


# =============================================================================
# 21. ВЛОЖЕННЫЙ LIST COMPREHENSION
# =============================================================================
#
# comprehension внутри comprehension — для матриц, комбинаций:
#
# matrix = [[1, 2], [3, 4], [5, 6]]
# flat = [n for row in matrix for n in row]
# # [1, 2, 3, 4, 5, 6]
#
# JS: matrix.flat()  или  matrix.flatMap(row => row)
#
# pairs = [(x, y) for x in range(3) for y in range(2)]
# # [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]
#
# таблица умножения 3×3:
# table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# # [[1,2,3], [2,4,6], [3,6,9]]
#
# читается справа налево: for row in matrix, потом for n in row.


# =============================================================================
# 22. DICT COMPREHENSION
# =============================================================================
#
# {ключ: значение for элемент in последовательность}
#
# nums = [1, 2, 3]
# squares_dict = {n: n ** 2 for n in nums}
# # {1: 1, 2: 4, 3: 9}
#
# names = ["Анна", "Борис", "Вика"]
# name_lengths = {name: len(name) for name in names}
# # {"Анна": 4, "Борис": 5, "Вика": 4}
#
# с фильтром:
# evens_only = {n: n ** 2 for n in range(10) if n % 2 == 0}
#
# JS: Object.fromEntries(arr.map(n => [n, n ** 2]))


# =============================================================================
# 23. SET COMPREHENSION
# =============================================================================
#
# {выражение for элемент in последовательность}
# фигурные скобки, но без двоеточия — это set, не dict!
#
# nums = [1, 2, 2, 3, 3, 3]
# unique_squares = {n ** 2 for n in nums}
# # {1, 4, 9}  — дубликаты убраны автоматически
#
# letters = {c.lower() for c in "Hello"}
# # {"h", "e", "l", "o"}


# =============================================================================
# 24. GENERATOR EXPRESSION (КРАТКО)
# =============================================================================
#
# те же скобки, но круглые () вместо [] — ленивый генератор, не список:
#
# gen = (n ** 2 for n in range(1000000))   # не создаёт список сразу
# first = next(gen)                         # 0
#
# sum(n ** 2 for n in range(10))           # скобки можно опустить в функции
#
# когда нужен именно список — используй [].
# когда только пройтись один раз (sum, max, any) — () экономит память.


# =============================================================================
# 25. КОГДА НЕ СТОИТ ИСПОЛЬЗОВАТЬ COMPREHENSION
# =============================================================================
#
# ✅ простые map/filter — отлично подходит
# ✅ короткие выражения — читаемо
#
# ❌ слишком длинная строка — лучше обычный for
# ❌ побочные эффекты (print, append в другой список) — только for
# ❌ сложная логика с break/continue — только for
# ❌ вложенность больше 2 уровней — трудно читать
#
# плохо:
# result = [do_something(x) for x in [y for y in data if y > 0] if x % 2 == 0]
#
# хорошо:
# positives = [y for y in data if y > 0]
# result = [do_something(x) for x in positives if x % 2 == 0]


# =============================================================================
# 26. ЛОВУШКИ ДЛЯ ТЕХ, КТО ПРИШЁЛ С JS
# =============================================================================
#
# Python                          JavaScript
# -----------------------------------------------
# for x in arr:                   for (const x of arr)
# for i in range(n):              for (let i = 0; i < n; i++)
# for i, x in enumerate(arr):     arr.forEach((x, i) => ...)
# while x < 10:                   while (x < 10)
# break / continue                break / continue
# else у цикла                    нет аналога
# x += 1                          x++
# [n * 2 for n in arr]            arr.map(n => n * 2)
# [n for n in arr if n > 0]       arr.filter(n => n > 0)
# {n: n**2 for n in arr}          Object.fromEntries(...)
# {n**2 for n in arr}             new Set(arr.map(...))
# (n**2 for n in arr)             function* generator — ленивый
#
# --- частые ошибки ---
#
# ❌ for i in range(10) { ... }     → фигурных скобок нет, только отступы
# ❌ range(1, 10) ждёт 10           → range(1, 11) для 1..10 включительно
# ❌ удалять из списка в for по нему же:
#    for x in my_list:
#        my_list.remove(x)         → индексы съедут, пропустишь элементы
#    ✅ for x in my_list[:]:       → иди по копии
# ❌ while True без break           → бесконечный цикл
# ❌ забыть счётчик += 1 в while    → тоже бесконечный цикл
# ❌ путать for/while с if          → for/while повторяют, if — один раз
# ❌ [for n in nums]                → нет выражения слева
# ❌ [n * 2 for n in nums if n > 0 if n < 10]  → два if подряд нельзя
# ✅ [n * 2 for n in nums if 0 < n < 10]
# ❌ путать фильтр и тернарник:
#    [n if n > 0 for n in nums]       → SyntaxError
# ✅ [n for n in nums if n > 0]       → фильтр
# ✅ [n if n > 0 else 0 for n in nums]  → тернарник в выражении
# ❌ {} пустой — это dict, не set
# ✅ set() — пустое множество
# ❌ break/continue в comprehension   → нельзя, только в for/while
#
# ✅ range(len(arr)) или enumerate(arr) — для индексов
# ✅ sum(), min(), max() — часто заменяют простой цикл
# ✅ list comprehension — короткая замена for + append


# =============================================================================
# 27. ЗАДАЧИ
# =============================================================================

# --- Циклы: сумма чисел от 1 до n ---
# n = 5
# total = 0
# for i in range(1, n + 1):
#     total += i
# # total = 15


# --- Циклы: сумма списка через sum (без цикла) ---
# nums = [1, 2, 3, 4, 5]
# total = sum(nums)


# --- Циклы: найти максимум в списке ---
# nums = [3, 7, 2, 9, 1]
# maximum = nums[0]
# for n in nums:
#     if n > maximum:
#         maximum = n
# # maximum = 9


# --- Циклы: посчитать чётные ---
# nums = [1, 2, 3, 4, 5, 6]
# count = 0
# for n in nums:
#     if n % 2 == 0:
#         count += 1
# # count = 3


# --- Циклы: FizzBuzz ---
# for n in range(1, 16):
#     if n % 15 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)


# --- Циклы: таблица умножения 3×3 ---
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i * j, end="\t")
#     print()


# --- Циклы: сумма цифр числа ---
# number = 12345
# total = 0
# for digit in str(number):
#     total += int(digit)
# # total = 15


# --- Циклы: while — угадай число (упрощённо) ---
# secret = 7
# guess = 0
# while guess != secret:
#     guess = int(input("Угадай число: "))
# print("Верно!")


# --- Циклы: break — найти первое число > 10 ---
# nums = [3, 8, 12, 5, 20]
# result = None
# for n in nums:
#     if n > 10:
#         result = n
#         break
# # result = 12


# --- Циклы: continue — вывести только нечётные ---
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
# # 1, 3, 5, 7, 9


# --- Циклы: цикл по словарю — найти самого старшего ---
# dict_age = {"Антон": 20, "Борис": 25, "Виктор": 15}
# oldest = None
# max_age = 0
# for name, age in dict_age.items():
#     if age > max_age:
#         max_age = age
#         oldest = name
# # oldest = "Борис"


# --- Comprehension: удвоить все числа ---
# nums = [1, 2, 3]
# doubled = [n * 2 for n in nums]
# # doubled = [2, 4, 6]


# --- Comprehension: только чётные ---
# nums = [1, 2, 3, 4, 5, 6]
# evens = [n for n in nums if n % 2 == 0]
# # evens = [2, 4, 6]


# --- Comprehension: квадраты нечётных от 1 до 10 ---
# squares = [n ** 2 for n in range(1, 11) if n % 2 != 0]
# # squares = [1, 9, 25, 49, 81]


# --- Comprehension: длины слов длиннее 3 букв ---
# words = ["hi", "hello", "hey", "python", "go"]
# long_words = [w for w in words if len(w) > 3]
# # long_words = ["hello", "python"]


# --- Comprehension: «even» / «odd» для каждого числа ---
# nums = [1, 2, 3, 4]
# labels = ["even" if n % 2 == 0 else "odd" for n in nums]
# # labels = ["odd", "even", "odd", "even"]


# --- Comprehension: расплющить матрицу ---
# matrix = [[1, 2], [3, 4], [5, 6]]
# flat = [n for row in matrix for n in row]
# # flat = [1, 2, 3, 4, 5, 6]


# --- Comprehension: словарь «число → квадрат» ---
# squares_dict = {n: n ** 2 for n in range(1, 6)}
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# --- Comprehension: сумма чисел, делящихся на 3 или 5 ---
# a, b = 1, 10
# result = sum([x for x in range(a, b + 1) if x % 3 == 0 or x % 5 == 0])
# # result = 33


# --- Comprehension: заменить отрицательные на 0 ---
# nums = [3, -1, 5, -7, 0]
# cleaned = [n if n >= 0 else 0 for n in nums]
# # cleaned = [3, 0, 5, 0, 0]


# --- Comprehension: FizzBuzz (упрощённо) ---
# fizzbuzz = [
#     "FizzBuzz" if n % 15 == 0 else
#     "Fizz" if n % 3 == 0 else
#     "Buzz" if n % 5 == 0 else
#     n
#     for n in range(1, 16)
# ]


# =============================================================================
# 28. РЕШЁННЫЕ ПРИМЕРЫ (можно запустить файл)
# =============================================================================

# print("--- for + range ---")
# for i in range(5):
#     print(i, end=" ")
# print()

# print("\n--- for по списку ---")
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# print("\n--- enumerate ---")
# for i, fruit in enumerate(fruits, start=1):
#     print(f"{i}. {fruit}")

# print("\n--- накопление суммы ---")
# nums = [1, 2, 3, 4, 5]
# total = 0
# for n in nums:
#     total += n
# print(f"Сумма: {total}")

# print("\n--- while ---")
# count = 0
# while count < 3:
#     print(f"count = {count}")
#     count += 1

# print("\n--- break ---")
# for i in range(10):
#     if i == 5:
#         break
#     print(i, end=" ")
# print("(остановились на 5)")

# print("\n--- map: удвоить ---")
# doubled = [n * 2 for n in [1, 2, 3]]
# print(doubled)

# print("\n--- filter: чётные ---")
# evens = [n for n in range(10) if n % 2 == 0]
# print(evens)

# print("\n--- map + filter ---")
# result = [n * 2 for n in range(10) if n % 2 == 0]
# print(result)

# print("\n--- тернарник в выражении ---")
# labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
# print(labels)

# print("\n--- dict comprehension ---")
# squares = {n: n ** 2 for n in range(1, 6)}
# print(squares)

# print("\n--- flatten matrix ---")
# matrix = [[1, 2], [3, 4]]
# flat = [n for row in matrix for n in row]
# print(flat)


# my_dict = {"one": 111, "two": 222, "three": 333}
# for i in my_dict.items():
#     dict_key = i[0]


# orders = [
#     {"номер": "001", "клиент": "John", "дата": "2022-01-01", "статус": "в обработке"},
#     {"номер": "002", "клиент": "Alice", "дата": "2022-01-02", "статус": "выполнен"},
#     {"номер": "003", "клиент": "Bob", "дата": "2022-01-03", "статус": "выполнен"},
#     {"номер": "004", "клиент": "Eva", "дата": "2022-01-04", "статус": "в обработке"},
# ]
# for index, order in enumerate(orders, start=1):
#     print(f"Заказ {index}:")
#     print(order.items())
#     for key, value in order.items():
#         print(f"{key}: {value}")
#     print()

""" Задача
В переменных a и b сохранено два целых положительных числа, таких что a <= b. Напишите программу, которая находит сумму всех чисел от a до b, кратных 3 или 5. Сохраните сумму в переменную result. Если между a и b нет таких чисел, то сохраните в result 0. """

# a = 1
# b = 10
# result = 0
# for x in range(a,b+1):
#     print(x)
#     if x % 3 == 0 or x % 5 == 0:
#         result+=x
# 
# или
# 
# result = sum([x for x in range(a,b+1) if x % 3 == 0 or x % 5 == 0])
# print(result)

""" Задача
Напишите программу на Python, которая определяет, является ли заданное число num простым. Простое число — это число, больше единицы, которое делится только на 1 и на само себя.

Если num — простое число, то сохраните в переменную result строку "это простое число". Если число не простое, то сохраните в переменную result строку "это не простое число".

Используйте цикл для решения этой задачи.

# Пример 1
num = 7
result = "это простое число"

# Пример 2
num = 8
result = "это не простое число"

# Пример 3
num = -7
result = "это не простое число"
 """

# num = 6
# data=[]

# if num<=1:
#     result = "это простое число"
# else:
#     for x in range(2,num+1):
#         if num % x == 0:
#             data.append(x)
#     result = "это простое число" if len(data) == 1 else "это не простое число"


# arr_nums = [x for x in range(2,num) if num % x == 0]
# result = "это простое число" if num > 1 and not arr_nums else "это не простое число"

""" Задача
Чтение и понимание чужого кода — это важный навык для программиста. Перед тем, как изменять или расширять функциональность программы, вам нужно хорошо понимать первоначальный замысел автора. Чтение и исправление кода других разработчиков помогает улучшить навыки осмысления кода и разбора его на части.

Вы вместе с коллегой Петром разрабатываете программу. Вам нужно написать скрипт, который будет проверять, является ли число степенью двойки. Петр прислал вам код, который возвращает неверный результат, помогите Петру исправить скрипт.

number = 16 # число для теста

if number == 0:
    is_two_power = False
while number % 2 == 0:
    number = number / 2
is_two_power = number == 0


Задача:

В переменной number сохранено число, напишите код, который проверят, является ли number степенью двойки? Ряд степеней двойки:

1, 2, 4, 8, 16, 32, 64 ...

Результат проверки True или False сохраните в переменную is_two_power. """


# if number == 0:
#     is_two_power = False
# else:
#     while number % 2 == 0:
#         number = number / 2
#     is_two_power = number == 1


""" Задача
Дан список чисел a.  Напишите программу, которая вернет True, если в списке больше нечетных чисел, и False — во всех остальных случаях. Результат сохраните в result.  """

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = True

# even = []
# odd = []

# for x in a:
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
# result = len(odd) > len(even)
# или
# result = sum([(1 if x % 2 == 0 else -1) for x in a]) < 0

""" Задача
Напишите программу, принимающую в виде аргументов два списка lst_1 и lst_2 и определяющую, являются ли они противоположными друг другу. Результат проверки сохраните в result в формате True или False.

Каждая пара списков будет состоять из двух одинаковых элементов (типа a и b). Список считается анти-списком, если все элементы в нем противоположны соответствующим элементам в первом списке.  

lst_1 = ["1", "0", "0", "1"]
lst_2 = ["0", "1", "1", "0"]
result = True

lst_1 = [3, 4]
lst_2 = [4, 3]
result = True

lst_1 = [1, 1]
lst_2 = [2, 2]
result = True

lst_1 = [1, 2]
lst_2 = [2, 2]
result = False


"""

# result = True

# if len(lst_1) != len(lst_2):
#     result = False
# else:
#     for i in range(len(lst_1)):
#         if lst_1[i] == lst_2[i]:
#             result = False
#             break






""" Задача
Есть словарь grades, содержащий информацию о школьных предметах и их оценках. В список good_subjects  сохраните названия всех предметов, у которых оценка больше или равна 4. 


 """
grades = {"Математика": 4, "История": 3, "Биология": 3, "География": 4}
# good_subjects = ["Математика", "География"]

# grades = {"Алгебра": 3, "ИЗО": 2}
# good_subjects = []

# for key, value in grades.items():
#     if value >= 4:
#         good_subjects.append(key)
# или
# good_subjects = [k for k , v in grades.items() if v >=4]
# print(good_subjects)

# НЕСОКОЛЬКО ЗАДАЧ НА DICT COMPREHENSION
# nums = [1, 2, 3, 4, 5, 8]
""" Квадраты чисел
# получить: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} """

# data = {n: n ** 2 for n in nums}

"""  Только чётные
nums = [1, 2, 3, 4, 5, 6]
# получить: {2: 2, 4: 4, 6: 6}  """
nums = [1, 2, 3, 4, 5, 6]
data = {n: n for n in nums if n%2 == 0}

""" Длина слов

words = ["cat", "python", "hi", "code"]
# получить: {"cat": 3, "python": 6, "hi": 2, "code": 4} """
words = ["cat", "python", "hi", "code"]
data = {w:len(w)for w in words}

""" Фильтр словаря

prices = {"apple": 50, "banana": 30, "grape": 80, "pear": 25}
# оставить только товары дороже 40:
# {"apple": 50, "grape": 80} """
prices = {"apple": 50, "banana": 30, "grape": 80, "pear": 25}
data = {k:v for k,v in prices.items() if v > 40}

""" Скидка 10%

prices = {"apple": 50, "banana": 30, "grape": 80}
# ключи те же, значения со скидкой 10%:
# {"apple": 45.0, "banana": 27.0, "grape": 72.0} """

prices = {"apple": 50, "banana": 30, "grape": 80}
data = {k:v-(v*0.1) for k,v in prices.items()  }

""" students = {"Anna": 5, "Bob": 3, "Kate": 4, "Max": 2}
# словарь «имя → зачёт/незачёт»:
# {"Anna": "зачёт", "Bob": "незачёт", ...}  — зачёт если оценка >= 4 """
students = {"Anna": 5, "Bob": 3, "Kate": 4, "Max": 2}
data = { k:"зачет" if v>=4 else "незачёт" for k,v in students.items() }

""" Задача
Напишите программу, которая принимает словарь input_dict и возвращает строку вида: ключ=значение&ключ=значение 

Строка должна быть лексикографически отсортирована по ключам исходного словаря. Сохраните полученный ответ в result. 


 """
input_dict = {'lesson': 2, 'task': 21, 'course': 'python'}
# sorted_dict = {}
# result = ""

# for k in sorted(input_dict):
#     sorted_dict[k] = input_dict[k]

# for k,v in sorted_dict.items():
#     result+=f"{k}={v}&"

# res = result[:-1]

# res = 'course=python&lesson=2&task=21'

# result = "&".join(f"{k}={input_dict[k]}" for k  in sorted(input_dict))

""" Задача
Напишите программу, которая принимает одну строку input_str и возвращает другую result, в которой каждая буква исходной строки повторяется дважды.

Пример:

input_str = "String"
result = "SSttrriinngg" """
input_str = "String"
# result = ""

# for x in input_str:
#     result+=f"{x}{x}"

result = "".join(f"{x}{x}" for x in input_str)

""" Задача
Напишите программу, которая будет принимать число n и проверять, кратна ли каждая его цифра цифре, стоящей слева от нее. Ответ сохраните в result в виде массива булевых значений результатов проверок.

result всегда должен начинаться с False, так как слева от первой цифры ничего нет. 

Пример:

n = 54412
result = [False, False, True, False, True] """
n = 54412
digits = [int(x) for x in str(n)]
result = [False]

for i in range(1, len(digits)):
    if digits[i-1] != 0:
        result.append(digits[i] % digits[i-1] == 0)
    else:
        result.append(False)  # Если предыдущая цифра 0 — всегда False, на 0 делать нельзя
    

"""
Задача:

В словареstudents сохранены данные про студентов, ключ — фамилия, значение — число баллов за экзамен, создайте список students_order, в котором каждый элемент это кортеж (tuple) с номером выступления студента и его фамилией. В students_order должны быть только те студенты, у которых более 90 баллов. Порядок определяется сортировкой по фамилии.

 students = {'Бабаков': 80, 'Антонов': 99, 'Волгов': 100}
students_order = [(1, 'Антонов'), (2, 'Волгов')] """

students = {'Бабаков': 80, 'Антонов': 99, 'Волгов': 100}

students_order =[]

# for i, name in enumerate(sorted(k for k, v in students.items() if v > 90), start=1):
#     students_order.append((i, name))

students_order = [name for name in sorted(students.keys()) if students[name] > 90]
students_order = list(enumerate(students_order, 1))

my_string = 'zis jqd qbdx qjjgsd bcd zjm fbc bvbx'
secret_dict = {
'v': 'w',
'x': 'y',
'i': 'h',
'q': 'l',
'c': 'n',
'b': 'a',
'f': 'r',
'j': 'o',
's': 'e',
'z': 't',
'g': 'k'}

# decrypted_string = 'the old lady looked and tom ran away'
decrypted_string = ""
for x in my_string:
    decrypted_string += secret_dict.get(x, x)  # если ключа нет — оставляем символ
# for x in my_string:
#     if(x != " " and x in secret_dict):
#         decrypted_string+= secret_dict[x]
#     elif(x != " " and not x in secret_dict):
#         decrypted_string+=x
#     else:
#         decrypted_string+= " "



