# Золотое правило:
# Генератор → когда каждый элемент входной коллекции дает ровно один элемент на выходе

# Цикл → когда:

# Нужно накапливать данные (группировка, подсчет сумм)

# Нужно изменять существующий словарь/список

# Есть сложная логика (несколько условий, вложенные операции)

# Визуальное сравнение:

# ГЕНЕРАТОР - плоская структура
# вход:  [A, B, C, D]
#        ↓  ↓  ↓  ↓
# выход: [a, b, c, d]  # каждый вход → один выход

# # ЦИКЛ - структура с накоплением
# вход:    [A, B, C, D]
#          ↓  ↓  ↓  ↓
# выход:  {A: [B, C], D: [...]}  # один ключ собирает много значений

""" comprehensions в Python по сути то же, что вы уже знаете в JS, только другой синтаксис.

Главная идея
Comprehension = map + filter в одной строке

Python	JavaScript
[x*2 for x in arr]
arr.map(x => x*2)
[x for x in arr if x>0]
arr.filter(x => x>0)
[x*2 for x in arr if x>0]
arr.filter(x=>x>0).map(x=>x*2)
List comprehension → map / filter
# Python
[x ** 2 for x in numbers]
// JS
numbers.map(x => x ** 2)
# Python
[x for x in numbers if x % 2 == 0]
// JS
numbers.filter(x => x % 2 === 0)
Dict comprehension → Object.fromEntries + map
# Python
{x: x**2 for x in numbers}
// JS
Object.fromEntries(numbers.map(x => [x, x**2]))
# Python
{word: len(word) for word in words}
// JS
Object.fromEntries(words.map(word => [word, word.length]))
Из словаря список → Object.keys / values / entries
# Python
[k for k in person]
[v for v in person.values()]
// JS
Object.keys(person)
Object.values(person)
Как запомнить тип результата
Смотрите только на внешние скобки:

[ ... ]           # список  → как [...arr.map()]
{ k: v ... }      # словарь → как Object.fromEntries(...)
{ x ... }         # set     → как new Set(arr.map(...))
Шпаргалка «если забыл»
Нужен массив → [выражение for x in ...]
Нужен объект → {ключ: значение for x in ...}
Есть условие → ... if условие в конце (как filter)
Есть if/else внутри → a if cond else b for x in ... (как тернарник)
["even" if x % 2 == 0 else "odd" for x in numbers]

numbers.map(x => x % 2 === 0 ? "even" : "odd") """

# Traditional way of creating a list with squares of numbers
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x ** 2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]

numbers = [1, 2, 3, 4, 5]
labelled_numbers = []
for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")
print(labelled_numbers)  # Outputs: ['odd', 'even', 'odd', 'even', 'odd']

labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labelled_numbers)  # Outputs: ['odd', 'even', 'odd', 'even', 'odd']

square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)  # Outputs: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = []
for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)
print(transpose)  # Outputs: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose)  # Outputs: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
