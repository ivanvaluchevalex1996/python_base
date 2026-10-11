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

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    reshaped_matrix = []
    arr = []
    rows, cols = new_shape
    for sub_matrix in a:
        for el in sub_matrix:
            arr.append(el)

    if rows * cols != len(arr):
        return []

    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(arr[x*cols+y])
        reshaped_matrix.append(row)    
    return reshaped_matrix

print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        dd = []
        for vector in matrix:
            sums = 0
            for num in vector:
                sums+=num
            dd.append(sums/len(vector))
    elif mode == "column":
        dd = [sum(col)/len(col) for col in zip(*matrix)]
       

    return dd      

	# return means

asd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# qwe = 'row'
qwe = 'column'

print(calculate_matrix_mean(asd, qwe))

matrix1 = [[1, 2], [3, 4]]
scalar1 = 2

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    dd = []
    for vector in matrix:
        new_vector = []
        for num in vector:
            new_num = num * scalar
            new_vector.append(new_num)
        dd.append(new_vector)    
    return dd

# print(scalar_multiply(matrix1, scalar1))  

matrix2 = [[4, 7], [2, 6]]
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    one, two = matrix
    det = one[0]* two[1] - one[1]* two[0]
    if det == 0:
        return None
    else:
        reverse_matrix = [[two[1]/det, -one[1]/det], [-two[0]/det, one[0]/det]]
        return reverse_matrix

# print(inverse_2x2(matrix2))


def make_diagonal(x):
    rows1 = len(x)
    print("🟢🔵🔴 ~ make_diagonal ~ rows1:", rows1)
    # for x in range(rows1):

print(make_diagonal([1,2,3]))