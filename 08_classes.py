# 🔴🔴🔴 УРОК 10: КЛАССЫ (OOP)
#
# Зачем классы:
# - объединить ДАННЫЕ + ПОВЕДЕНИЕ в одном месте
# - создать много похожих объектов по одному шаблону
# - в ML: Dataset, Model, Trainer, Pipeline — часто классы
#
# Функция  = действие
# Класс    = чертёж объекта
# Объект   = конкретный экземпляр по чертежу
#
# JS:
# class User { constructor(name) { this.name = name; } }


# =============================================================================
# 1. ЗАЧЕМ КЛАССЫ (а не только dict + функции)
# =============================================================================
#
# Можно так:
#   user = {"name": "Anna", "age": 25}
#   def greet(user): ...
#
# Но класс удобнее, когда:
# - у сущности много связанных данных
# - есть методы (действия над этими данными)
# - нужно много экземпляров одного типа
# - нужна иерархия (наследование)



# =============================================================================
# 2. class — ОБЪЯВЛЕНИЕ КЛАССА
# =============================================================================
#
# class ИмяКласса:
#     тело
#
# Имена классов — PascalCase: User, DataLoader, LinearModel
# (функции/переменные — snake_case)

print("--- 2. простой класс ---")


class Dog:
    pass  # пустой класс (пока)


d = Dog()
print(type(d))   # <class '__main__.Dog'>
print(d)         # объект в памяти


# =============================================================================
# 3. АТРИБУТЫ ЭКЗЕМПЛЯРА
# =============================================================================
#
# Атрибут = данные объекта (как поля / свойства)
# Можно задать снаружи, но правильно — через __init__

print("\n--- 3. атрибуты ---")

dog = Dog()
dog.name = "Rex"
dog.age = 3
print(dog.name, dog.age)


# =============================================================================
# 4. __init__ — КОНСТРУКТОР
# =============================================================================
#
# Вызывается АВТОМАТИЧЕСКИ при создании: Dog(...)
# self — сам объект (в JS это this)
#
# ⚠️ self пишется первым параметром метода ВСЕГДА
# При вызове dog.bark() Python сам передаёт self

print("\n--- 4. __init__ ---")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


rex = Dog("Rex", 3)
bob = Dog("Bob", 5)
print(rex.name, rex.age)
print(bob.name, bob.age)


# =============================================================================
# 5. МЕТОДЫ — функции внутри класса
# =============================================================================
#
# Метод всегда получает self — доступ к данным объекта

print("\n--- 5. методы ---")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: гав!")

    def birthday(self):
        self.age += 1
        return self.age


rex = Dog("Rex", 3)
rex.bark()
print("age after birthday:", rex.birthday())


# =============================================================================
# 6. self — ЧТО ЭТО
# =============================================================================
#
# self = текущий экземпляр
#
# rex.bark()   ≈   Dog.bark(rex)
#
# Без self метод не знает, ЧЕЙ name / age брать.
# Имя self — соглашение (можно другое, но так не делают).


# =============================================================================
# 7. АТРИБУТЫ КЛАССА vs ЭКЗЕМПЛЯРА
# =============================================================================
#
# Атрибут класса  — общий для всех объектов (на классе)
# Атрибут экземпляра — свой у каждого (через self)

print("\n--- 7. class vs instance attrs ---")


class Dog:
    species = "canis"          # атрибут КЛАССА (общий)

    def __init__(self, name):
        self.name = name       # атрибут ЭКЗЕМПЛЯРА (личный)


a = Dog("Rex")
b = Dog("Bob")
print(a.species, b.species)    # оба canis
print(a.name, b.name)          # разные


# =============================================================================
# 8. __str__ и __repr__ — как объект печатается
# =============================================================================
#
# Без них print(obj) → <Dog object at 0x...>
# __str__  — для людей (print)
# __repr__ — для разработчиков / отладки

print("\n--- 8. __str__ ---")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog(name={self.name!r}, age={self.age})"


print(Dog("Rex", 3))


# =============================================================================
# 9. ИНКАПСУЛЯЦИЯ (договорённости Python)
# =============================================================================
#
# Публичное:     name
# «Внутреннее»:  _name      (не трогай снаружи без нужды)
# «Приватное»:   __name     (name mangling: _Class__name)
#
# В Python нет жёсткого private как в Java — это соглашения.

print("\n--- 9. инкапсуляция ---")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # «protected» по соглашению

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be > 0")
        self._balance += amount

    def get_balance(self):
        return self._balance


acc = BankAccount("Anna", 100)
acc.deposit(50)
print(acc.owner, acc.get_balance())


# =============================================================================
# 10. @property — атрибут через метод
# =============================================================================
#
# Чтобы читать как поле: obj.balance
# но внутри — логика / вычисление / защита

print("\n--- 10. @property ---")


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        self._balance = value


acc = BankAccount(100)
print(acc.balance)     # getter
acc.balance = 200      # setter
print(acc.balance)
# acc.balance = -1     # ValueError


# =============================================================================
# 11. НАСЛЕДОВАНИЕ — class Child(Parent)
# =============================================================================
#
# Child получает методы/атрибуты Parent.
# Можно переопределить (override) и вызвать super().

print("\n--- 11. наследование ---")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return f"{self.name}: гав!"


class Cat(Animal):
    def speak(self):
        return f"{self.name}: мяу!"


animals = [Dog("Rex"), Cat("Mur"), Animal("??")]
for a in animals:
    print(a.speak())   # полиморфизм: один интерфейс, разное поведение


# =============================================================================
# 12. super() — вызвать родителя
# =============================================================================

print("\n--- 12. super() ---")


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # сначала инициализация родителя
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.breed})"


print(Dog("Rex", "labrador"))


# =============================================================================
# 13. isinstance / issubclass
# =============================================================================

print("\n--- 13. isinstance ---")
print(isinstance(Dog("Rex", "lab"), Dog))      # True
print(isinstance(Dog("Rex", "lab"), Animal))   # True (наследование)
print(issubclass(Dog, Animal))                 # True


# =============================================================================
# 14. МЕТОДЫ: instance / classmethod / staticmethod
# =============================================================================
#
# instance method   — обычный, есть self
# @classmethod      — первый аргумент cls (сам класс), часто фабрики
# @staticmethod     — просто функция в пространстве имён класса (нет self/cls)

print("\n--- 14. classmethod / staticmethod ---")


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def c_to_f(c):
        return c * 9 / 5 + 32


t = Temperature.from_fahrenheit(68)
print(round(t.celsius, 1))
print(Temperature.c_to_f(20))


# =============================================================================
# 15. ДАТАКЛАССЫ — меньше бойлерплейта (Python 3.7+)
# =============================================================================
#
# Когда класс в основном хранит данные — @dataclass пишет
# __init__ / __repr__ / сравнение за тебя.

print("\n--- 15. dataclass ---")

from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    active: bool = True


u = User("Anna", 25)
print(u)
print(u.name, u.active)


# =============================================================================
# 16. МАГИЧЕСКИЕ МЕТОДЫ (часто полезные)
# =============================================================================
#
# __init__   создание
# __str__    print(obj)
# __repr__   отладка
# __len__    len(obj)
# __eq__     obj == other
# __getitem__ obj[i]
#
# Полный список огромный — учи по мере нужды.

print("\n--- 16. magic methods ---")


class Team:
    def __init__(self, members):
        self.members = list(members)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, i):
        return self.members[i]


team = Team(["Anna", "Bob", "Kate"])
print(len(team))
print(team[0])
for name in team:          # работает благодаря __getitem__
    print("-", name)


# =============================================================================
# 17. ПАТТЕРНЫ ДЛЯ ML (как классы используют в деле)
# =============================================================================

print("\n--- 17. ML patterns ---")


class StandardScaler:
    """Как идея sklearn: fit на train, transform на любых данных."""

    def __init__(self):
        self.mean_ = None
        self.std_ = None

    def fit(self, X):
        # X: list[list[float]] или позже numpy
        cols = list(zip(*X))
        self.mean_ = [sum(c) / len(c) for c in cols]
        self.std_ = [
            (sum((x - m) ** 2 for x in c) / len(c)) ** 0.5
            for c, m in zip(cols, self.mean_)
        ]
        return self

    def transform(self, X):
        return [
            [(x - m) / (s or 1.0) for x, m, s in zip(row, self.mean_, self.std_)]
            for row in X
        ]

    def fit_transform(self, X):
        return self.fit(X).transform(X)


X_train = [[1.0, 10.0], [3.0, 30.0], [5.0, 50.0]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
print("scaled:", X_scaled)
print("mean_:", scaler.mean_)


@dataclass
class LinearModel:
    """Мини-модель: y = w·x + b (один признак для простоты)."""
    w: float = 0.0
    b: float = 0.0

    def predict(self, x):
        return self.w * x + self.b

    def fit_closed_form(self, xs, ys):
        # упрощённо: w = cov/var, b = mean_y - w*mean_x
        n = len(xs)
        mean_x = sum(xs) / n
        mean_y = sum(ys) / n
        var_x = sum((x - mean_x) ** 2 for x in xs) / n
        cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / n
        self.w = cov / (var_x or 1.0)
        self.b = mean_y - self.w * mean_x
        return self


model = LinearModel().fit_closed_form([1, 2, 3], [2, 4, 6])
print("predict(10):", model.predict(10))


# =============================================================================
# 18. КОГДА НЕ НУЖЕН КЛАСС
# =============================================================================
#
# ❌ Не делай класс ради класса
# ✅ Функция — если одно действие без состояния
# ✅ dict / dataclass — если только данные
# ✅ class — если есть состояние + методы + жизненный цикл (fit/predict)


# =============================================================================
# 19. ЧЕКЛИСТ МЛ-ИНЖЕНЕРА ПО КЛАССАМ
# =============================================================================
#
# ✅ ОБЯЗАТЕЛЬНО:
# 1. class / объект / экземпляр
# 2. __init__ + self
# 3. методы экземпляра
# 4. наследование + super()
# 5. __str__ / __repr__
# 6. isinstance
# 7. @dataclass для простых структур
# 8. паттерн fit / transform / predict
#
# ⬜ ПОЛЕЗНО:
# - @property
# - @classmethod / @staticmethod
# - ABC (абстрактные классы) — позже
# - __call__ — объект как функция (часто в PyTorch modules)
#
# Правило:
# данные без поведения → dataclass / dict
# данные + поведение → class


# =============================================================================
# 20. МИНИ-ПРАКТИКА (раскомментируй и реши)
# =============================================================================
#
# 1) Класс Book(title, author, year) + __str__
# 2) Метод is_old(self, current_year) → True если книге > 50 лет
# 3) Класс Library: список книг, методы add_book / find_by_author
# 4) Наследование: EBook(Book) с полем file_size_mb
# 5) @dataclass Point(x, y) и метод distance_to(other)
#
# class Book:
#     ...
