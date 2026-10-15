import numpy as np


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    result = []
    n_cols_a = len(a[0])
    len_b = len(b)
    if n_cols_a != len_b:
        return -1

    for row in a:
        element = sum(i * j for i, j in zip(row, b))
        result.append(element)
    return result


a = [[1, 2], [2, 4]]
b = [1, 2]

# print(matrix_dot_vector(a,b))


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    transposed = []
    n_rows = len(a)  # Количество строк исходной матрицы (2)
    n_cols = len(a[0])  # Количество столбцов исходной матрицы (3)

    for col_idx in range(n_cols):
        new_row = []
        for row_idx in range(n_rows):
            new_row.append(a[row_idx][col_idx])
        transposed.append(new_row)
    return transposed


a = [[1, 2, 3], [4, 5, 6]]
# print(transpose_matrix(a))


def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    reshaped_matrix = []
    flat = []
    n_rows, n_cols = new_shape
    for row in a:
        for element in row:
            flat.append(element)

    if n_rows * n_cols != len(flat):
        return []

    for row_idx in range(n_rows):
        row = []
        for col_idx in range(n_cols):
            row.append(flat[row_idx * n_cols + col_idx])
        reshaped_matrix.append(row)
    return reshaped_matrix


# print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (4, 2)))


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means = []
        for row in matrix:
            row_sum = 0
            for num in row:
                row_sum += num
            means.append(row_sum / len(row))
    elif mode == "column":
        means = [sum(col) / len(col) for col in zip(*matrix)]

    return means


# return means

matrix_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mean_mode = 'row'
mean_mode = "column"

# print(calculate_matrix_mean(matrix_example, mean_mode))

matrix1 = [[1, 2], [3, 4]]
scalar1 = 2


def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    result = []
    for row in matrix:
        new_row = []
        for num in row:
            new_num = num * scalar
            new_row.append(new_num)
        result.append(new_row)
    return result


# print(scalar_multiply(matrix1, scalar1))

matrix2 = [[4, 7], [2, 6]]


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    row0, row1 = matrix
    det = row0[0] * row1[1] - row0[1] * row1[0]
    if det == 0:
        return None
    else:
        inverse_matrix = [
            [row1[1] / det, -row0[1] / det],
            [-row1[0] / det, row0[0] / det],
        ]
        return inverse_matrix


# print(inverse_2x2(matrix2))


def make_diagonal(x):
    diagonal_matrix = []
    n = len(x)
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(x[i])
            else:
                row.append(0)
        diagonal_matrix.append(row)
    return diagonal_matrix


# x = [1, 2, 3]
# output = make_diagonal(x)
# print("🟢🔵🔴 ~ output:", output)
