# 🔴🔴🔴 УРОК 2: СПИСКИ И МНОЖЕСТВА


# =============================================================================
# 1. СРЕЗЫ СПИСКА
# =============================================================================
#
# students_data[0:2]   # с 0 по 1 (2 не включается)
# students_data[:2]    # с начала до 1
# students_data[1:]    # с 1 до конца
# students_data[-1]    # последний элемент
# students_data[::2]   # элементы с чётными индексами (0, 2, 4...)
# students_data[::-1]  # список в обратном порядке (новая копия)
#
# students_data = ["1", "2", "3"]
# print(students_data[1:])    # ["2", "3"]
# print(students_data[0:2])   # ["1", "2"]
#
# срез создаёт новый список, оригинал не меняется:
# part = students_data[1:]
# students_data.append("4")   # part не изменится


# =============================================================================
# 1.1. RANGE — генерация последовательности чисел
# =============================================================================
#
# range(start, stop, step)  — stop НЕ включается (как в срезах!)
#
# list(range(5))            # [0, 1, 2, 3, 4]
# list(range(1, 4))         # [1, 2, 3]       — 4 не входит
# list(range(0, 11, 2))     # [0, 2, 4, 6, 8, 10]
# list(range(5, 0, -1))     # [5, 4, 3, 2, 1]
#
# до N включительно:        range(a, N + 1)
# вниз до 0 включительно:   range(a, -1, -step)
#
# в цикле range часто без list():
# for i in range(3):
#     print(i)              # 0, 1, 2
#
# сумма от a до b включительно:
# result = sum(range(a, b + 1))


# =============================================================================
# 2. МЕТОДЫ СПИСКА (аналог Array в JS)
# =============================================================================
#
# append(x)           — добавить в конец.           JS: arr.push(x)
# extend(items)         — добавить несколько.         JS: arr.push(...items)
# insert(i, x)          — вставить по индексу.        JS: arr.splice(i, 0, x)
# pop()                 — убрать последний.           JS: arr.pop()
# pop(i)                — убрать по индексу.          JS: arr.splice(i, 1)[0]
# remove(x)             — убрать по значению.         JS: arr.splice(arr.indexOf(x), 1)
# clear()               — очистить список.            JS: arr.length = 0
#
# len(arr)              — длина.                       JS: arr.length
# x in arr              — есть ли элемент.            JS: arr.includes(x)
# arr.index(x)          — индекс первого вхождения.    JS: arr.indexOf(x)
# arr.index(x, start, end) — поиск в диапазоне [start, end)
# arr.count(x)          — сколько раз встречается x.   JS: arr.filter(v => v === x).length
# arr.copy()            — копия списка.                JS: [...arr]
# arr.sort()            — сортировка на месте.         JS: arr.sort()
# arr.reverse()         — развернуть на месте.         JS: arr.reverse() (возвращает массив, в Python — None)
#
# del arr[i]            — удалить по индексу.          JS: delete нет, используй splice
# del arr[i:j]          — удалить срез
#
# встроенные функции для списков:
# sum(arr)              — сумма.                       JS: arr.reduce((a, b) => a + b)
# min(arr) / max(arr)   — минимум / максимум.          JS: Math.min(...arr)
# sorted(arr)           — новый отсортированный список
# list(arr)             — преобразовать в список
# reversed(arr)         — итератор в обратном порядке  JS: arr.toReversed()
#
# students_data = ["1", "2", "3"]
# students_data.append("4")           # ["1", "2", "3", "4"]
# students_data.extend(["5", "6"])    # ["1", "2", "3", "4", "5", "6"]
# students_data.insert(1, "new")      # ["1", "new", "2", "3", "4", "5", "6"]
# students_data.pop()                 # убрать последний
# students_data.remove("new")         # убрать по значению


# =============================================================================
# 3. СОРТИРОВКА, КОПИЯ, ОБЪЕДИНЕНИЕ
# =============================================================================
#
# sort() / sorted()
# nums.sort()                      # по возрастанию, меняет список
# nums.sort(reverse=True)          # по убыванию
# nums.sort(key=len)               # по длине строк
# nums.sort(key=abs)               # по модулю числа
# sorted(nums)                     # новый список, оригинал не меняется
# sorted(nums, reverse=True)       # новый список по убыванию
#
# sort() возвращает None!          # ❌ wrong = nums.sort()
#
# копия
# new_list = my_list.copy()        # JS: [...myList]
# new_list = my_list[:]            # то же через срез
#
# объединение
# combined = list_1 + list_2       # новый список. JS: [...a, ...b]
# list_1.extend(list_2)            # дописать в существующий. JS: a.push(...b)
#
# ловушка append vs extend:
# arr.append([4, 5])               # [1, 2, 3, [4, 5]]  — вложенный список!
# arr.extend([4, 5])               # [1, 2, 3, 4, 5]    — добавляет элементы
#
# повторение
# zeros = [0] * 3                  # [0, 0, 0]
#
# ссылки и копии (как в JS с массивами):
# b = a                            # та же ссылка, не копия!
# b = a.copy()                     # shallow copy (поверхностная)
# import copy
# b = copy.deepcopy(a)             # deep copy — для вложенных списков
#
# nums = [3, 1, 2]
# nums.sort()                      # [1, 2, 3]
# nums.reverse()                   # [3, 2, 1]


# =============================================================================
# 3.1. ЦИКЛЫ ПО СПИСКУ
# =============================================================================
#
# for x in my_list:                # JS: for (const x of arr)
#     print(x)
#
# for i in range(len(my_list)):    # JS: for (let i = 0; i < arr.length; i++)
#     print(my_list[i])
#
# for i, x in enumerate(my_list):  # индекс + значение
#     print(i, x)                  # JS: arr.forEach((x, i) => ...)
#
# не удаляй элементы в цикле по тому же списку — индексы съедут:
# for x in my_list[:]:             # иди по копии — безопаснее
#     ...


# =============================================================================
# 4. LIST COMPREHENSION (аналог map / filter в JS)
# =============================================================================
#
# JS: nums.map(n => n * 2)
# doubled = [n * 2 for n in [1, 2, 3]]           # [2, 4, 6]
#
# JS: nums.filter(n => n % 2 === 0)
# evens = [n for n in [1, 2, 3, 4] if n % 2 == 0]  # [2, 4]
#
# map + filter вместе:
# result = [n * 2 for n in nums if n % 2 == 0]


# =============================================================================
# 5. МНОЖЕСТВА (set) — аналог Set в JS
# =============================================================================
#
# s = {1, 2, 3}              # set с элементами
# s = set([1, 2, 2, 3])      # {1, 2, 3} — дубликаты убираются
# empty = set()              # пустой set (не {} — это dict!)
#
# s.add(x)                   # JS: s.add(x)
# s.remove(x)                # удалить x; ValueError, если x нет
# s.discard(x)               # удалить x; если x нет — ничего не делает
#
# remove vs discard (оба только для set, у list есть только remove):
# s = {1, 2, 3}
# s.remove(2)    # {1, 3}
# s.discard(99)  # {1, 3} — ошибки нет
# s.remove(99)   # ❌ ValueError
#
# когда что:
# remove — уверен, что элемент есть (иначе это ошибка логики)
# discard — «убери, если есть» (безопаснее)
# s.pop()                    # убрать случайный элемент
# s.clear()                  # очистить
# x in s                     # JS: s.has(x)
# len(s)                     # JS: s.size
#
# операции над множествами (оба операнда — set!):
# a = {1, 2, 3}
# b = {3, 4, 5}
#
# объединение — все уникальные из a и b:
# a | b              # {1, 2, 3, 4, 5}
# a.union(b)         # то же самое
#
# пересечение — только общие элементы:
# a & b              # {3}
# a.intersection(b)  # {3}
#
# разность — что есть в a, но нет в b:
# a - b              # {1, 2}
# a.difference(b)    # {1, 2}
# b - a              # {4, 5}  — порядок важен!
#
# симметричная разность — только в одном из двух:
# a ^ b              # {1, 2, 4, 5}
#
# один элемент — оберни в { }:
# students = {'Анна', 'Борис', 'Вика'}
# students | {'Глеб'}        # новый set, students не меняется
# students - {'Борис'}       # новый set без Бориса
# students | 'Глеб'          # ❌ TypeError — строка не set
#
# изменить students на месте:
# students |= {'Глеб'}       # добавить (как add, но через операцию)
# students -= {'Борис'}      # убрать (как discard, но через операцию)
# students = students | {'Глеб'}   # то же через переприсвоение
#
# задача «добавить одного, убрать другого» — два способа:
# students.add(new_student)
# students.discard(churn_student)
# # или:
# students |= {new_student}
# students -= {churn_student}
#
# добавить много элементов из другого set:
# a.update(b)        # a |= b — дописать все из b в a
# a <= b             # True, если все элементы a есть в b
# убрать дубликаты из списка:
# unique = list(set(my_list)) # JS: [...new Set(arr)]
#
# list vs set — когда что:
# list  — порядок, дубликаты, доступ по индексу
# set   — уникальность, быстрый поиск, операции | & -


# =============================================================================
# 6. FROZENSET — неизменяемое множество
# =============================================================================
#
# my_frozenset = frozenset([1, 2, 3])
# множества можно вычитать друг из друга:
# frozenset({1, 3, 5} - {1})  # frozenset({3, 5})


# =============================================================================
# 6.1. ЛОВУШКИ ДЛЯ ТЕХ, КТО ПРИШЁЛ С JS
# =============================================================================
#
# 1. range(a, b) — b не включается          → до 100: range(a, 101)
# 2. sort() / reverse() возвращают None     → копия: sorted(arr) или arr[::-1]
# 3. {} — это dict, не set                  → пустой set: set()
# 4. = для списков — ссылка, не копия       → копия: arr.copy()
# 5. append([1,2]) ≠ extend([1,2])          → append вложит список целиком
# 6. индексы с 0 (как в JS), не с 1
# 7. splice ≈ insert / pop / del, но разделены на разные методы
# 8. arr.includes(x)  →  x in arr
# 9. arr.length       →  len(arr)
# 10. [...a, ...b]    →  a + b


# =============================================================================
# 7. ЗАДАЧИ
# =============================================================================

# --- Задача: index и подсчёт ---
# my_list = [1, 2, 11, 10, 10]
# eleven_index = my_list.index(11)
# ten_count = my_list.count(10)
# # или: ten_count = sum(1 for x in my_list if x == 10)


# --- Задача: сумма чисел от a до b включительно ---
# a = 1
# b = 3
# result = sum(range(a, b + 1))  # 6


# --- Задача: элементы списка по индексам ---
# my_list = ["Anatoly", "Fedor", 1, 2, 3]
# first_item = my_list[0]
# last_item = my_list[-1]
# reversed_list = my_list[::-1]
# even_items = my_list[::2]


# --- Задача: удалить 2-й, 5-й и последний элемент (удалять с конца!) ---
# scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# scores.pop(9)  # последний
# scores.pop(4)  # пятый из исходного
# scores.pop(1)  # второй из исходного


# --- Задача: range ---
# var_1 = list(range(-100, 101))
# var_2 = list(range(250, -1, -2))
# var_3 = list(range(101, 201, 2))  # нечётные от 100 до 200


# --- Задача: sorted, set, frozenset ---
# numbers_list = [1, 5, 3, 3, 5]
# numbers_list_ordered = sorted(numbers_list, reverse=True)
# numbers_set = set(numbers_list)
# numbers_set.add(max(numbers_list) + 1)
# numbers_frozenset = frozenset(set(numbers_list) - {min(numbers_list)})
# # numbers_list_ordered = [5, 5, 3, 3, 1]
# # numbers_set = {1, 3, 5, 6}
# # numbers_frozenset = frozenset({3, 5})


# --- Задача: объединить и отсортировать два списка ---
# list_1 = [1, 5, 3]
# list_2 = [2, 8]
# list_1.sort()
# list_2.sort(reverse=True)
# list_3 = list_1 + list_2
# list_3.sort()
# list_3_len = len(list_3)
# # list_1 = [1, 3, 5]
# # list_2 = [8, 2]
# # list_3 = [1, 2, 3, 5, 8]
# # list_3_len = 5

# 
a = [1, 2, 4, 3]

length_half = len(a) / 2
print(length_half)

sum_left = 3
sum_right = 7
result = False