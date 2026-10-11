import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)
	theta = np.linalg.inv(X.T @ X) @ X.T @ y
	return theta

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
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
    m, n = X.shape # (3,2)
    y = y.reshape(-1, 1)  # Приводим y к вектору-столбцу
    theta = np.zeros((n, 1))  # Инициализируем веса нулями // [0, 0]

    
    # Здесь ваш код: реализуйте градиентный спуск
    for _ in range(iterations):
        # # 1. Предсказание (3,)
        # pred = X @ theta
        # # 2. Ошибки (3,) - так как и pred, и y теперь одномерные, вычитание идет идеально
        # error = pred - y
        # # 3. Сырой градиент: сумма (признак × ошибка), ещё без деления на m
        # raw_gradient = X.T @ error
        # # 4. Градиент: та же сумма, усреднённая по объектам
        # gradient = (1 / m) * raw_gradient
        # # 5. Обновление весов
        # theta = theta - alpha * gradient

        for _ in range(iterations):
            pred = X @ theta
            grad = 1/m * (X.T @ (pred - y))
            theta = theta - alpha * grad
      

    return theta.flatten()

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([3, 5, 7])
alpha = 0.1
iterations = 1

print(linear_regression_gradient_descent(X, y, alpha, iterations))
