import numpy as np


def linear_regression_normal_equation(
    X: list[list[float]], y: list[float]
) -> list[float]:
    X = np.array(X)
    y = np.array(y)
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta


# X = np.array([[1, 1], [1, 2], [1, 3]])
# y = np.array([3, 5, 7])
# alpha = 0.1
# iterations = 1000


def linear_regression_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float,
    iterations: int,
) -> np.ndarray:
    """
    Выполняет линейную регрессию методом градиентного спуска.

    Аргументы:
        X: Матрица признаков формы (m, n), где первый столбец состоит из единиц (для свободного члена)
        y: Вектор целевых значений формы (m,)
        alpha: Скорость обучения (learning rate)
        iterations: Количество итераций градиентного спуска

    Возвращает:
        Обученные веса в виде одномерного массива формы (n,)
    """
    m, n = X.shape  # (3,2)
    y = y.reshape(-1, 1)  # Приводим y к вектору-столбцу
    theta = np.zeros((n, 1))  # Инициализируем веса нулями // [0, 0]

    # Здесь ваш код: реализуйте градиентный спуск
    for _ in range(iterations):
        # # 1. Предсказание (3,)
        # pred = X @ theta
        # # 2. Ошибки (3,) - так как и pred, и y теперь одномерные, вычитание идет идеально
        # error = pred - y
        # # 3. Сырой градиент: сумма (признак × ошибка), ещё без деления на m
        # в питоне нельзя умножать матрицу напрямую матрицу признаков на ошибку, потому что они разных размеров поэтому нужно траснпонирование
        # Матричное умножение по определению работает только по правилу «СТРОКА умножается на СТОЛБЕЦ».
        # raw_gradient = X.T @ error
        # # 4. Градиент: та же сумма, усреднённая по объектам
        # gradient = (1 / m) * raw_gradient
        # # 5. Обновление весов
        # theta = theta - alpha * gradient

        for _ in range(iterations):
            pred = X @ theta
            grad = 1 / m * (X.T @ (pred - y))
            theta = theta - alpha * grad

    return theta.flatten()


# print(linear_regression_gradient_descent(X, y, alpha, iterations))


def feature_scaling(
    data: np.ndarray,
) -> (np.ndarray, np.ndarray):
    # Your code here
    mu = np.mean(data, axis=0)
    diff_quad_sum = np.sum((data - mu) ** 2, axis=0)
    sigma = np.sqrt(diff_quad_sum / data.shape[0])
    # или кратко sigma = np.std(data, axis=0)
    standardized_data = (data - mu) / sigma

    x_min = np.min(data, axis=0)
    x_max = np.max(data, axis=0)

    normalized_data = (data - x_min) / (x_max - x_min)

    return (
        standardized_data,
        normalized_data,
    )


# data = np.array([[1, 2], [3, 4], [5, 6]])

# print(feature_scaling(data))


def shuffle_data(X, y, seed=None):
    # Your code here
    # permutation возврщает новый список, в отличии от shuffle
    if seed is not None:
        np.random.seed(seed)
    idx = np.random.permutation(len(X))  # например [2, 0, 3, 1]
    # X_shuffled = np.array([X[el] for el in idx])
    # y_shuffled = np.array([y[el] for el in idx])
    # return X_shuffled, y_shuffled
    #   или кратко чероз возможность NumPy
    return X[idx], y[idx]


# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# y = np.array([1, 2, 3, 4])
# print(shuffle_data(X, y))


def batch_iterator(X, y=None, batch_size=64):
    # Your code here
    dd = []
    for i in range(0, len(X), batch_size):
        new_list_x = X[i : i + batch_size]
        if y is not None:
            new_list_y = y[i : i + batch_size]
            dd.append([new_list_x, new_list_y])
        else:
            dd.append(new_list_x)
    return dd


# X = np.array(
#     [
#         [1, 2],
#         [3, 4],
#         [5, 6],
#         [7, 8],
#         [9, 10],
#     ]
# )
# y = np.array([1, 2, 3, 4, 5])
# y = None
# batch_size = 2
# batch_iterator(X, y, batch_size)
#  [
#     [[[1, 2], [3, 4]], [1, 2]],
#     [[[5, 6], [7, 8]], [3, 4]],
#     [[[9, 10]], [5]],
# ]
# print(batch_iterator(X,y, batch_size))


def to_categorical(x, n_col: int | None = None):
    # Your code here
    max_num_label = np.max(x)
    if n_col is None:
        col = max_num_label + 1
    else:
        col = n_col
    zeros_list = np.zeros((len(x), col))
    for i in range(len(zeros_list)):
        # по питоновски
        # zeros_list[i][x[i]] = 1
        # по нампаевски
        zeros_list[i, x[i]] = 1
    return zeros_list


x = np.array([0, 1, 2, 1, 0])

# print(to_categorical(x, 2))
# print(to_categorical(x))


def accuracy_score(y_true, y_pred):
    # Your code here
    dd = y_true == y_pred
    sums = np.sum(dd)
    acuracy = sums / len(y_true)
    return acuracy


# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 0, 1, 0, 1])
# output = accuracy_score(y_true, y_pred)
# print(output)


def precision(y_true, y_pred):
    # Your code here
    dd = y_true + y_pred
    TP = (dd == 2).sum()
    FP = ((y_pred == 1) & (y_true == 0)).sum()
    if TP == 0:
        return 0
    else:
        return TP / (TP + FP)


# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])

# result = precision(y_true, y_pred)
# print(result)


def recall(y_true, y_pred):
    # Your code here
    dd = y_true + y_pred
    TP = (dd == 2).sum()
    FN = ((y_pred == 0) & (y_true == 1)).sum()
    if TP == 0:
        return 0
    else:
        return TP / (TP + FN)


# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])

# print(recall(y_true, y_pred))


def f_score(y_true, y_pred, beta):
    dd = y_true + y_pred
    TP = (dd == 2).sum()
    FN = ((y_pred == 0) & (y_true == 1)).sum()
    FP = ((y_pred == 1) & (y_true == 0)).sum()
    recall = 0 if TP == 0 else TP / (TP + FN)
    precision = 0 if TP == 0 else TP / (TP + FP)
    if precision == 0 and recall == 0:
        return 0
    return (1 + beta**2) * recall * precision / (recall + (beta**2 * precision))


def ridge_loss(
    X: np.ndarray,
    w: np.ndarray,
    y_true: np.ndarray,
    alpha: float,
) -> float:
    # Your code here
    pred = X @ w
    loss = np.sum((y_true - pred) ** 2) / len(y_true)
    L2 = alpha * np.sum(w**2)
    return loss + L2


# X = np.array([[1, 2], [3, 4], [5, 6]])
# w = np.array([1, 0.5])
# y_true = np.array([3, 7, 11])
# alpha = 0.1

# loss = ridge_loss(X, w, y_true, alpha)
# print(loss)


def kernel_function(x1, x2):
    # Your code here
    return x1 @ x2


x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])

# result = kernel_function(x1, x2)
# print(result)

def gini_impurity(y):
    
	return round(val,3)
