"""Тренажёр: `*`, `@`, `np.dot` — формы и смысл.

Конспекты: ynote/a.NumPy/11.умножение — star, at, dot.md (всё: @, *, ML)

Как учить: в каждой задаче допиши `...` (одна–две строки), запусти файл.
Все assert должны пройти. Можно сначала угадать форму на бумаге, потом проверить в REPL: `arr.shape`.
"""

import numpy as np


# --- 1. Поэлементно: два вектора ---
# Верни поэлементное произведение [1,2,3] и [10,20,30].
def task01_elementwise_1d() -> np.ndarray:
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])
    return a * b


assert np.array_equal(task01_elementwise_1d(), [10, 40, 90])


# --- 2. Скалярное произведение: @ и dot на 1D ---
# Одно число — сумма произведений пар.
def task02_dot_1d() -> float:
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    return a @ b


assert task02_dot_1d() == 32.0


# --- 3. Форма после `*` (broadcast) ---
# X: 3 объекта, 2 признака; w: 2 веса. Какой shape у X * w?
def task03_shape_star() -> tuple[int, ...]:
    X = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    w = np.array([2.0, 3.0])
    return np.array(X * w).shape


assert task03_shape_star() == (3, 2)


# --- 4. `*` + sum = один логит на объект ---
# Должно совпасть с X @ w (без bias).
def task04_star_sum_equals_at() -> bool:
    X = np.array([[1.0, 2.0], [3.0, 4.0]])
    w = np.array([1.0, 0.5])
    z_from_star = (X * w).sum(axis=1)
    z_from_at = X @ w
    return np.allclose(z_from_star, z_from_at)


assert task04_star_sum_equals_at() is True


# --- 5. Матрица @ вектор (как в Deep-ML #24) ---
def task05_matvec_shape() -> tuple[int, ...]:
    X = np.ones((3, 2))
    w = np.ones(2)
    z = X @ w
    return z.shape


assert task05_matvec_shape() == (3,)


# --- 6. Матрица @ столбец весов ---
# Числа те же, что в задаче 5, но форма другая.
def task06_matvec_column_shape() -> tuple[int, ...]:
    X = np.ones((3, 2))
    w = np.ones((2, 1))
    z = X @ w
    return z.shape


assert task06_matvec_column_shape() == (3, 1)


# # --- 7. np.dot vs @ на (m,n) и (n,) ---
# def task07_dot_same_as_at() -> bool:
#     X = np.array([[1.0, 0.0], [1.0, 1.0]])
#     w = np.array([2.0, 3.0])
#     return np.allclose(np.dot(X, w), ...)


# assert task07_dot_same_as_at() is True


# # --- 8. Два логита на объект: (2,3) @ (3,2) ---
# # Подсказка: «середины 3=3 → (2,2)». Проверь один элемент.
# def task08_matmul_one_entry() -> float:
#     A = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])  # (2, 3)
#     W = np.ones((3, 2))  # (3, 2)
#     out = ...  # A @ W
#     return float(out[0, 0])


# assert task08_matmul_one_entry() == 1.0


# # --- 9. Поймай несовпадение внутренних размеров ---
# # (2,3) @ (2,) — нельзя (3 != 2). Верни True, если при X @ w вылетает ValueError.
# def task09_inner_dims_must_match() -> bool:
#     X = np.ones((2, 3))
#     w = np.ones(2)
#     try:
#         ...  # X @ w
#         return False
#     except ValueError:
#         return True


# assert task09_inner_dims_must_match() is True


# # --- 10. Мини-нейрон: z для батча ---
# # Те же идеи, что single_neuron: только z, без sigmoid.
# def task10_batch_logits() -> list[float]:
#     features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
#     weights = [0.7, -0.4]
#     bias = -0.1
#     X = np.array(features)
#     w = np.array(weights)
#     z = ...  # X @ w + bias
#     return [round(float(v), 4) for v in z]


# assert task10_batch_logits() == [-0.15, -0.35, 0.7]
