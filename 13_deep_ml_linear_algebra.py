def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    data = []
    stolb_len_a = len(a[0])
    len_b = len(b)
    if stolb_len_a != len_b:
        return -1
    
    for x in a:
        el = sum(i*j for i,j in zip(x,b))
        data.append(el)
    return data
a = [[1, 2], [2, 4]] 
b = [1, 2]

# print(matrix_dot_vector(a,b))

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    dd = []
    rows = len(a)     # Количество строк исходной матрицы (2)
    cols = len(a[0])  # Количество столбцов исходной матрицы (3)

    for i in range(cols):
        new_row = []
        for x in range(rows):
            new_row.append(a[x][i])
        dd.append(new_row)
    return dd
            
            
a = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(a))