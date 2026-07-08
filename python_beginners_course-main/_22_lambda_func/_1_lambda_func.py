""" сравнивать с JS, так и надо.

Запомни один шаблон для Python:

lambda x: ...
Это буквально как в JS:

x => ...
Быстрая шпаргалка JS → Python
x => x.age → lambda x: x["age"] (если dict)
(a, b) => a - b → lambda a, b: a - b
arr.map(x => x * 2) → map(lambda x: x * 2, arr)
(или по-питоновски лучше: [x * 2 for x in arr])
arr.filter(x => x > 0) → filter(lambda x: x > 0, arr)
(или [x for x in arr if x > 0]) """
ё
def sort_by_len(element: str) -> int:
    return len(element)


sort_by_len_lambda = lambda element: len(element)
print(sort_by_len("banana"))  # Output: 6
print(sort_by_len_lambda("banana"))  # Output: 6


fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, key=lambda element: len(element))

fruits = ["apple", "banana", "cherry", "date"]
longest_word = max(fruits, key=lambda x: len(x))
print(longest_word)  # Output: 'banana'
