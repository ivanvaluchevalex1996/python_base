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


def calculate_dot_product(vec1, vec2):
    # Your code here
    dot = 0
    for i in range(len(vec1)):
        dot += vec1[i] * vec2[i]
    return dot


# vec1 = np.array([1, 2, 3])
# vec2 = np.array([4, 5, 6])
# output = calculate_dot_product(vec1, vec2)
# print("🟢🔵🔴 ~ output:", output)


def compressed_row_sparse_matrix(dense_matrix):
    values = []
    col_indices = []
    row_ptr = [0]
    for row in dense_matrix:
        for col_idx, num in enumerate(row):
            if num != 0:
                values.append(num)
                col_indices.append(col_idx)
        row_ptr.append(len(values))

    return (values, col_indices, row_ptr)


# dense_matrix = [[1, 0, 0, 0], [0, 2, 0, 0], [3, 0, 4, 0], [1, 0, 0, 5]]

# vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
# print("Values array:", vals)
# print("Column indices array:", col_idx)
# print("Row pointer array:", row_ptr)


def orthogonal_projection(v, L):
    v = np.array(v, dtype=float)
    L = np.array(L, dtype=float)
    # proj_L(v) = ((v · L) / (L · L)) * L
    scalar = (v @ L) / (L @ L)
    projection = scalar * L
    return [round(x, 3) for x in projection]


# v = [3, 4]
# L = [1, 0]
# print(orthogonal_projection(v, L))  # [3.0, 0.0]


def compressed_col_sparse_matrix(dense_matrix):
    values = []
    row_indices = []
    col_ptr = [0]
    n_cols = len(dense_matrix[0])
    n_rows = len(dense_matrix)

    for col in range(n_cols):
        for row_idx in range(n_rows):
            value = dense_matrix[row_idx][col]
            if value != 0:
                values.append(value)
                row_indices.append(row_idx)
        col_ptr.append(len(values))
    return (values, row_indices, col_ptr)


# dense_matrix = [[0, 0, 3, 0], [1, 0, 0, 4], [0, 2, 0, 0]]

# values, row_indices, col_ptr = compressed_col_sparse_matrix(dense_matrix)


def cosine_similarity(v1, v2):
    dot = v1 @ v2
    norm_v1 = np.sqrt(v1 @ v1)
    norm_v2 = np.sqrt(v2 @ v2)

    # Implement your code here
    return dot / (norm_v1 * norm_v2)


# v1 = np.array([1, 2, 3])
# v2 = np.array([2, 4, 6])
# print(round(cosine_similarity(v1, v2), 3))


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    P = np.linalg.inv(C) @ B
    return P


def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    # Your code here

    result = []
    for value in data:
        powers = []
        for power in range(degree + 1):
            powers.append(value**power)
        result.append(powers)
    return result


data = [1.0, 2.0]
degree = 2
print(phi_transform(data, degree))
