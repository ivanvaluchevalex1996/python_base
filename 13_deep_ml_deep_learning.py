"""Deep-ML Deep Learning: https://www.deep-ml.com/"""

import math
import numpy as np


# #22 https://www.deep-ml.com/problems/22
def sigmoid(z: float) -> float:
    return round(1 / (1 + math.exp(-z)), 4)


assert sigmoid(0) == 0.5  # ожидаемо: 0.5


# ---------------------------------------------------------------------------
# Многоклассовая классификация: логиты z → вероятности p → потеря CE
# ---------------------------------------------------------------------------
# Три «этажа» выхода классификатора на ОДНОМ объекте:
#   1) логиты z — сырые оценки классов (до нормализации);
#   2) вероятности p = softmax(z), сумма по классам = 1        → задача #23;
#   3) log p — удобно для loss; считают стабильно из z         → задача #39 log_softmax.
#
# Cross-entropy на объекте с верным классом k — ВСЕГДА одно и то же число:
#   L = -log(p_k)
# Два способа посчитать (разный ВХОД, не разная формула):
#   • #134: на входе уже p (и one-hot y)     → clip(p) → -log(p у верного класса) → mean по батчу;
#   • обучение / PyTorch: на входе логиты z, метка — индекс k → loss = -log_softmax(z)[k]
#     (эквивалент: logsumexp(z) - z[k], без явного softmax→log).
#
# Когда что вызывать:
#   есть готовые вероятности     → #134, log_softmax НЕ нужен;
#   есть только логиты           → #39 (или logsumexp), softmax #23 для loss можно не вызывать отдельно.
#
# Отдельно: бинарная задача #22 sigmoid + #24 MSE — там один выход, не эта цепочка.


# #23 https://www.deep-ml.com/problems/23
# z (scores) → p. Стабильность: вычесть max(z) до exp.
def softmax(scores: list[float]) -> list[float]:
    data = [np.exp(n) for n in (np.array(scores) - max(scores))]
    sum_exp = sum(data)
    probs = [n / sum_exp for n in data]
    return probs


_out23 = softmax([1, 2, 3])
assert abs(sum(_out23) - 1.0) < 1e-6  # ожидаемо: сумма ≈ 1.0
assert [round(x, 4) for x in _out23] == [
    0.0900,
    0.2447,
    0.6652,
]  # ожидаемо: [0.0900, 0.2447, 0.6652]


# #39 https://www.deep-ml.com/problems/39
# z → log(p), без явного деления на sum(exp) и потом log (устойчивее).
# log_softmax(z)[k] = log(p_k); для CE: loss на объекте = -log_softmax(z)[k].
def log_softmax(scores: np.ndarray) -> np.ndarray:
    shifted = scores - np.max(scores)
    return shifted - np.log(np.sum(np.exp(shifted)))


_out39 = log_softmax(np.array([1.0, 2.0, 3.0]))
assert np.allclose(
    np.round(_out39, 4),
    [-2.4076, -1.4076, -0.4076],
)


# #134 https://www.deep-ml.com/problems/134
# Вход: готовые p (батч N×C) и one-hot y. CE = среднее по объектам -log(p_верный).
# clip(p, ε, 1-ε) — чтобы log(0) не дал -inf при нулевой вероятности.
def compute_cross_entropy_loss(
    predicted_probs: np.ndarray,
    true_labels: np.ndarray,
    epsilon: float = 1e-15,
) -> float:
    # Числ. устойчивость: p=0 → log(p)=-inf (и loss «взрывается»); p>1 — некорректные входы.
    # Ограничиваем p ∈ [ε, 1−ε] — в условии #134; для log(1) верхняя грань почти не меняет ответ.
    p = np.clip(predicted_probs, epsilon, 1.0 - epsilon)
    per_object = -np.sum(true_labels * np.log(p), axis=1)
    return float(np.mean(per_object))


# Пример A — «путь через p» (как на сдаче #134): softmax уже сделан, дают готовые вероятности + one-hot.
# Практически: -log(p у верного класса) и среднее по батчу → здесь 0.4338.
_pred134 = np.array([[0.7, 0.2, 0.1], [0.3, 0.6, 0.1]])
_lab134 = np.array([[1, 0, 0], [0, 1, 0]])
assert round(compute_cross_entropy_loss(_pred134, _lab134), 4) == 0.4338

# Пример B — «путь через z» (как в обучении): на входе только логиты, p явно не нужен.
# Тот же смысл L = -log(p_верный), но log p берём из log_softmax(#39); с A совпадает по числу.
_z_chain = np.array([1.0, 2.0, 3.0])
_p_chain = np.array(softmax(_z_chain.tolist()))
_y_chain = np.array([[1.0, 0.0, 0.0]])
_loss_via_p = compute_cross_entropy_loss(
    _p_chain.reshape(1, -1), _y_chain
)  # A: сначала softmax → p
_loss_via_z = -log_softmax(_z_chain)[0]  # B: сразу из z, класс 0
assert np.allclose(_loss_via_p, _loss_via_z, rtol=1e-4)  # оба ~2.4076

# ---------------------------------------------------------------------------


# #24 https://www.deep-ml.com/problems/24
# Single Neuron: для каждого примера z = w·x + b, p = sigmoid(z);
# вернуть probabilities и MSE(p, y), оба с round(..., 4).
def single_neuron_model(
    features: list[list[float]],
    labels: list[float],
    weights: list[float],
    bias: float,
) -> tuple[list[float], float]:
    X = np.array(features)
    w = np.array(weights)
    z = X @ w + bias
    sigm = 1 / (1 + np.exp(-z))
    sigm_round = np.round(sigm, 4)
    loss = np.mean((sigm_round - labels) ** 2)
    return (sigm_round, loss)


_out24 = single_neuron_model(
    features=[[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]],
    labels=[0, 1, 0],
    weights=[0.7, -0.4],
    bias=-0.1,
)
# assert _out24 == ([0.4626, 0.4134, 0.6682], 0.3349)


# #42 https://www.deep-ml.com/problems/42
# ReLU: Rectified Linear Unit — активация скрытых слоёв (d.4.1 §8–9.1).
# Один float z (сырое значение после w·x+b у нейрона): если z > 0 → вернуть z, иначе → 0.
# Формула: ReLU(z) = max(0, z). Поэлементно на векторе — то же правило на каждое число.
# Примеры: relu(0.0)→0.0, relu(1.0)→1.0, relu(-1.0)→0.0
def relu(z: float) -> float:
    return z if z > 0 else 0


assert relu(0.0) == 0.0
assert relu(1.0) == 1.0
assert relu(-1.0) == 0.0


# #44 https://www.deep-ml.com/problems/44
# Leaky ReLU: как ReLU (#42), но при z <= 0 не обнуляем, а умножаем на alpha (наклон «протечки»).
# Формула: z > 0 → z; иначе → alpha * z.  alpha по умолчанию 0.01.
# z=0 → 0. Примеры: (-1, α=0.01)→-0.01; (-2, α=0.1)→-0.2
def leaky_relu(z: float, alpha: float = 0.01) -> float:
    return z if z > 0 else alpha * z


# assert leaky_relu(0) == 0
# assert leaky_relu(1) == 1
# assert leaky_relu(-1) == -0.01
# assert leaky_relu(-2, alpha=0.1) == -0.2


# #96 https://www.deep-ml.com/problems/96
def hard_sigmoid(x: float) -> float:
    return max(0, min(1, 0.2 * x + 0.5))


# assert hard_sigmoid(0.0) == 0.5


# #97 https://www.deep-ml.com/problems/97
# ELU (Exponential Linear Unit): вариант ReLU для скрытых слоёв (d.4.1 §9.4).
# x > 0  → вернуть x (как ReLU #42).
# x <= 0 → alpha * (exp(x) - 1); при x=0 это 0; при x→-∞ выход → -alpha («пол»).
# alpha по умолчанию 1.0. Ответ round(..., 4).
# Пример: elu(-1) → -0.6321  (1 * (e^-1 - 1)).
def elu(x: float, alpha: float = 1.0) -> float:
    """
    Compute the ELU activation function.

    Args:
        x (float): Input value
        alpha (float): ELU parameter for negative values (default: 1.0)

    Returns:
        float: ELU activation value
    """
    # Your code here
    return x if x > 0 else round(alpha * (math.exp(x) - 1), 4)


assert round(elu(-1.0), 4) == -0.6321
assert elu(2.0) == 2.0
assert round(elu(0.0), 4) == 0.0


# #99 https://www.deep-ml.com/problems/99
# Softplus: гладкая аппроксимация ReLU (d.4.1 §9.4.2).
# Формула: log(1 + exp(x)) = ln(1 + e^x). Ответ round(..., 4).
# Наивно: math.log1p(math.exp(x)) — ОК для умеренных x; при больших x (напр. 800) exp переполняется.
# Стабильно: max(x, 0) + math.log1p(math.exp(-abs(x)))  — то же число, без overflow.
# Примеры: softplus(2) → 2.1269; при x→+∞ softplus≈x; при x→−∞ softplus→0.
# На Deep-ML в окне решения: import math (как для elu).
def softplus(x: float) -> float:
    return max(x, 0) + math.log1p(math.exp(-abs(x)))


# assert softplus(2) == 2.1269
# assert round(softplus(0), 4) == 0.6931  # ln(2)


# #100 https://www.deep-ml.com/problems/100
# Softsign: сжимающая активация, как tanh (d.4.1 §9.4.3), выход строго в (-1, 1).
# Формула: x / (1 + abs(x)). Без exp — только |x| и деление. round(..., 4).
# Пример: softsign(1) → 0.5  (1 / (1+1)).
# При x=9: softsign=0.9, tanh≈1 — softsign к ±1 подходит медленнее (хвост ~ 1/x).
def softsign(x: float) -> float:
    return round(x / (1 + abs(x)), 4)


# assert softsign(1) == 0.5
# assert softsign(0) == 0.0
# assert softsign(-2) == -0.6667


# #102 https://www.deep-ml.com/problems/102
# Swish (= SiLU в PyTorch): x * sigmoid(x) (d.4.1 §9.4.4). «Самогейт» — вход умножается на свой же σ(x).
# Формула: x / (1 + exp(-x)). Может быть < 0 при x < 0 (в отличие от ReLU). round(..., 4).
# Пример: swish(1) → 0.7311.
# На Deep-ML: import math (как для sigmoid #22).
def swish(x: float) -> float:
    return round(x / (1 + math.exp(-x)), 4)


# assert swish(1) == 0.7311
# assert swish(0) == 0.0


# #113 https://www.deep-ml.com/problems/113
# Residual block (ResNet-идея): shortcut = исходный x прибавляется к выходу «ветки».
# Порядок: h = ReLU(W1 @ x) → out = ReLU(W2 @ h + x). ReLU поэлементно: np.maximum(0, ...).
# Размеры: x — 1D (d,), W1 и W2 — (d, d), чтобы x + ... совпадал по длине.
# Пример: x=[1,2], W1=I, W2=0.5·I → [1.5, 3.0]. @ — матричное умножение (a.NumPy/11).
# NLP/Transformer: та же идея — sublayer(x) + x после attention/FFN.
def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    h = np.maximum(0, w1 @ x)
    return np.maximum(0, w2 @ h + x)


_x113 = np.array([1.0, 2.0])
_w1_113 = np.array([[1.0, 0.0], [0.0, 1.0]])
_w2_113 = np.array([[0.5, 0.0], [0.0, 0.5]])
assert np.allclose(residual_block(_x113, _w1_113, _w2_113), [1.5, 3.0])


# ---------------------------------------------------------------------------
# После многоклассовой CE (#134): BCE (#263) → производные σ (#217) → momentum (#146)
# ---------------------------------------------------------------------------


# #263 https://www.deep-ml.com/problems/263
# Бинарная классификация: метка y∈{0,1}, предсказание p = P(y=1) после sigmoid(#22), p∈(0,1).
# На одном объекте (см. #134, но один выход вместо one-hot по классам):
#   L_i = -[ y_i·log(p_i) + (1-y_i)·log(1-p_i) ]
# Батч: mean(L_i). clip(p)∈[ε,1-ε] — как в #134 (log(0) и log(1) ломают loss).
# Связь: #134 + softmax — много классов; здесь один нейрон + sigmoid → BCE.
# Пример: y_true=[1,0,1,0], y_pred=[0.9,0.1,0.8,0.2] → mean ≈ 0.1643
def binary_cross_entropy(
    y_true: list[float],
    y_pred: list[float],
    epsilon: float = 1e-15,
) -> float:
    # Your code here
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    p = np.clip(y_pred, epsilon, 1.0 - epsilon)
    loss = -(y_true * np.log(p) + (1.0 - y_true) * np.log(1.0 - p))
    return np.mean(loss)


assert (
    round(
        binary_cross_entropy([1, 0, 1, 0], [0.9, 0.1, 0.8, 0.2]),
        4,
    )
    == 0.1643
)


# #217 https://www.deep-ml.com/problems/217
# Backprop: градиент по входу слоя = (градиент дальше) × производная активации σ′(x).
# Здесь — только σ′ в точке x (одно число), словарь 'sigmoid' | 'tanh' | 'relu'.
#   sigmoid:  σ(x)·(1-σ(x))     при x=0 → 0.25
#   tanh:     1 - tanh(x)²      при x=0 → 1.0
#   relu:     1 если x>0 иначе 0   при x=0 → 0 (как в условии Deep-ML)
# У тебя уже σ(x) в #22; для tanh: math.tanh(x) или (math.exp(x)-math.exp(-x))/(...)
def activation_derivatives(x: float) -> dict[str, float]:
    s = 1 / (1 + math.exp(-x))
    t = math.tanh(x)
    return {
        "sigmoid": s * (1 - s),
        "tanh": 1 - t**2,
        "relu": 1.0 if x > 0 else 0.0,
    }


assert activation_derivatives(0.0) == {"sigmoid": 0.25, "tanh": 1.0, "relu": 0.0}


