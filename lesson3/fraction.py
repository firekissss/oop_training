"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerator}, {self.__denominator})"

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        new_num = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_den = self.__denominator * other.__denominator
        return Fraction(new_num, new_den)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        gcd = Fraction.gcd(self.__numerator, self.__denominator)

        self.__numerator //= gcd
        self.__denominator //= gcd

        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

        return self


# код для проверки
fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
