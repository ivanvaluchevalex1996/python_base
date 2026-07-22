# 🔴🔴🔴 УРОК 11: ОБРАБОТКА ОШИБОК (exceptions)
#
# Зачем:
# - программа не должна падать из-за плохого ввода / файла / сети
# - ошибку нужно ПОЙМАТЬ, ОБЪЯСНИТЬ или ПРОБРОСИТЬ выше
# - в ML: битый CSV, NaN, неверный shape, отсутствие файла модели
#
# Ошибка в Python = exception (исключение)
# JS: try / catch / finally — почти то же самое


# =============================================================================
# 1. ЧТО ТАКОЕ ИСКЛЮЧЕНИЕ
# =============================================================================
#
# Когда Python не может выполнить код — «бросает» исключение.
# Если его не поймать — программа останавливается с traceback.
#
# print(1 / 0)           → ZeroDivisionError
# int("abc")             → ValueError
# [1, 2][10]             → IndexError
# {"a": 1}["b"]          → KeyError
# open("no_file.txt")    → FileNotFoundError

print("--- 1. без обработки программа бы упала ---")
# print(1 / 0)  # раскомментируй и посмотри traceback


# =============================================================================
# 2. try / except — ПОЙМАТЬ ОШИБКУ
# =============================================================================
#
# try:
#     опасный код
# except SomeError:
#     что делать, если упало
#
# JS:
# try { ... } catch (e) { ... }

print("\n--- 2. try / except ---")

try:
    print(1 / 0)
except ZeroDivisionError:
    print("нельзя делить на ноль")

print("программа жива")


# =============================================================================
# 3. except Exception as e — ПОСМОТРЕТЬ СООБЩЕНИЕ
# =============================================================================

print("\n--- 3. as e ---")

try:
    int("hello")
except ValueError as e:
    print("тип:", type(e).__name__)
    print("текст:", e)


# =============================================================================
# 4. НЕСКОЛЬКО except
# =============================================================================
#
# Сначала более КОНКРЕТНЫЕ ошибки, потом общие.
# Порядок важен: Python берёт первый подходящий блок.

print("\n--- 4. несколько except ---")


def parse_int(text):
    try:
        return int(text)
    except ValueError:
        print(f"ValueError: {text!r} не число")
        return None
    except TypeError:
        print("TypeError: нужен str/bytes")
        return None


print(parse_int("42"))
print(parse_int("abc"))
print(parse_int(None))


# =============================================================================
# 5. ОДИН except НА НЕСКОЛЬКО ТИПОВ
# =============================================================================

print("\n--- 5. несколько типов в одном except ---")

try:
    x = int("x")
except (ValueError, TypeError) as e:
    print("ошибка ввода:", e)


# =============================================================================
# 6. else и finally
# =============================================================================
#
# else     — если в try НЕ было исключения
# finally  — выполнится ВСЕГДА (и при успехе, и при ошибке)
#            часто для закрытия файла / соединения

print("\n--- 6. else / finally ---")

try:
    n = int("10")
except ValueError:
    print("не число")
else:
    print("успех, n =", n)
finally:
    print("finally: всегда")


# =============================================================================
# 7. ЧАСТЫЕ ТИПЫ ОШИБОК (знать в лицо)
# =============================================================================
#
# ValueError          — значение не подходит (int("abc"))
# TypeError           — неверный тип (len(5))
# IndexError          — индекс вне списка
# KeyError            — нет ключа в dict
# AttributeError      — нет атрибута / метода у объекта
# ZeroDivisionError   — / 0
# FileNotFoundError   — файла нет
# PermissionError     — нет прав
# ImportError / ModuleNotFoundError
# AssertionError      — assert упал
# RuntimeError        — общая runtime-проблема
# StopIteration       — итератор закончился (обычно не ловят руками)
#
# Базовый класс почти всех: Exception


# =============================================================================
# 8. raise — БРОСИТЬ ОШИБКУ САМОМУ
# =============================================================================
#
# Когда входные данные невалидны — лучше упасть ЯСНО,
# чем тихо вернуть мусор.

print("\n--- 8. raise ---")


def normalize(x, mean, std):
    if std == 0:
        raise ValueError("std must not be 0")
    return (x - mean) / std


try:
    print(normalize(10, 5, 0))
except ValueError as e:
    print("поймали:", e)


# =============================================================================
# 9. raise ... from e — ЦЕПОЧКА ПРИЧИН
# =============================================================================
#
# Полезно, когда ловишь низкоуровневую ошибку
# и кидаешь свою, более понятную.

print("\n--- 9. raise from ---")


def load_threshold(text):
    try:
        return float(text)
    except ValueError as e:
        raise ValueError(f"bad threshold: {text!r}") from e


try:
    load_threshold("abc")
except ValueError as e:
    print(e)
    # print(e.__cause__)  # исходный ValueError от float()


# =============================================================================
# 10. СВОИ ИСКЛЮЧЕНИЯ — class MyError(Exception)
# =============================================================================
#
# В больших проектах делают свои типы ошибок,
# чтобы ловить именно их, а не всё подряд.

print("\n--- 10. custom exception ---")


class DataValidationError(Exception):
    """Данные для модели невалидны."""


class ShapeMismatchError(DataValidationError):
    """Несовместимые shape у X и y."""


def check_xy(X, y):
    if len(X) != len(y):
        raise ShapeMismatchError(
            f"len(X)={len(X)} != len(y)={len(y)}"
        )


try:
    check_xy([[1], [2]], [0])
except ShapeMismatchError as e:
    print("ML validation:", e)


# =============================================================================
# 11. assert — ПРОВЕРКА ДЛЯ РАЗРАБОТЧИКА
# =============================================================================
#
# assert условие, "сообщение"
# Если условие False → AssertionError
#
# ⚠️ assert можно отключить флагом python -O
# Для пользовательского ввода / API лучше raise ValueError

print("\n--- 11. assert ---")

n_features = 3
row = [1.0, 2.0, 3.0]
assert len(row) == n_features, "row has wrong length"
print("assert ok")


# =============================================================================
# 12. НЕ ДЕЛАЙ ТАК
# =============================================================================
#
# ❌ except:            — ловит ВСЁ, включая KeyboardInterrupt (плохо)
# ❌ except Exception:  — слишком широко, если потом не логируешь/не знаешь что делать
# ❌ проглатывать ошибку молча:
#       try: ...
#       except Exception:
#           pass
#
# ✅ лови конкретные ошибки
# ✅ пиши понятное сообщение / логируй
# ✅ если не знаешь что делать — пробрось выше (raise)


# =============================================================================
# 13. ПРАКТИЧЕСКИЕ ПАТТЕРНЫ
# =============================================================================

print("\n--- 13. практические паттерны ---")

# --- 13.1 Безопасный доступ к dict ---
user = {"name": "Anna"}
print(user.get("age", 0))          # лучше, чем try/except KeyError для простого случая

# --- 13.2 Файл может отсутствовать ---
from pathlib import Path

path = Path("model_weights.bin")
if not path.exists():
    print("файла модели нет (это ок для демо)")
else:
    text = path.read_text(encoding="utf-8")

# Эквивалент через исключение:
try:
    data = open("model_weights.bin", "rb").read()
except FileNotFoundError:
    data = None
    print("FileNotFoundError -> data=None")

# --- 13.3 Преобразование типов из CSV/UI ---
raw = ["10", "20", "x", "40"]
nums = []
for item in raw:
    try:
        nums.append(int(item))
    except ValueError:
        print("skip bad value:", item)
print("nums:", nums)

# --- 13.4 Контекстный менеджер (файлы) ---
# with сам закроет файл даже при ошибке (внутри finally)
try:
    with open("nope.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("with + FileNotFoundError обработан")


# =============================================================================
# 14. ЛОГИРОВАНИЕ ОШИБОК (вместо print в проде)
# =============================================================================

print("\n--- 14. logging ---")

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("деление сломалось")  # пишет traceback в лог


# =============================================================================
# 15. ПАТТЕРНЫ ДЛЯ ML
# =============================================================================

print("\n--- 15. ML patterns ---")


def train_test_split_sizes(n, test_ratio=0.2):
    if not 0 < test_ratio < 1:
        raise ValueError(f"test_ratio must be in (0, 1), got {test_ratio}")
    if n < 2:
        raise ValueError(f"need at least 2 samples, got n={n}")
    n_test = max(1, int(n * test_ratio))
    n_train = n - n_test
    if n_train < 1:
        raise ValueError("train set is empty — уменьши test_ratio")
    return n_train, n_test


print(train_test_split_sizes(100, 0.2))

try:
    train_test_split_sizes(100, 1.5)
except ValueError as e:
    print("bad split:", e)


def safe_accuracy(y_true, y_pred):
    if len(y_true) == 0:
        raise ValueError("y_true is empty")
    if len(y_true) != len(y_pred):
        raise ShapeMismatchError(
            f"len(y_true)={len(y_true)} != len(y_pred)={len(y_pred)}"
        )
    correct = sum(a == b for a, b in zip(y_true, y_pred))
    return correct / len(y_true)


print("acc:", safe_accuracy([0, 1, 1], [0, 1, 0]))


# =============================================================================
# 16. КОГДА ЛОВИТЬ, А КОГДА ПАДАТЬ
# =============================================================================
#
# Лови, если:
# - ошибка ОЖИДАЕМА (нет файла, плохой user input, таймаут сети)
# - ты можешь ВОССТАНОВИТЬСЯ (ретрай, дефолт, сообщение пользователю)
#
# Падай / пробрасывай, если:
# - это баг в логике (неверный shape внутри твоего кода)
# - на этом уровне ты не знаешь, что делать
#
# Правило ML:
# на границе системы (файл, API, UI) — валидируй и лови
# внутри модели/метрик — raise с понятным текстом


# =============================================================================
# 17. ЧЕКЛИСТ
# =============================================================================
#
# ✅ ОБЯЗАТЕЛЬНО:
# 1. try / except / else / finally
# 2. except SomeError as e
# 3. несколько except + порядок (сначала конкретные)
# 4. raise ValueError("...")
# 5. частые типы: ValueError, TypeError, KeyError, IndexError, FileNotFoundError
# 6. свои Exception для домена (DataValidationError)
# 7. не глотать ошибки молча
#
# ⬜ ПОЛЕЗНО:
# - raise from e
# - logging.exception
# - with для ресурсов
# - assert только для внутренних инвариантов
#
# JS ↔ Python:
# try/catch/finally  ≈  try/except/finally
# throw new Error()  ≈  raise Exception()


# =============================================================================
# 18. МИНИ-ПРАКТИКА (раскомментируй и реши)
# =============================================================================
#
# 1) Функция div(a, b): верни a/b, при b==0 верни None (через try/except)
# 2) Функция read_int(text): int(text) или raise ValueError с понятным текстом
# 3) Свой класс EmptyBatchError(Exception)
# 4) Функция batch_mean(nums): если список пуст — EmptyBatchError, иначе среднее
# 5) Прочитай файл "data.txt"; если нет — создай с текстом "ok" и прочитай снова
#
# def div(a, b):
#     ...
