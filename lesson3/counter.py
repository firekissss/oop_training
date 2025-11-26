"""
Напишите класс Counter, имеющий следующие методы:

- __init__(self): конструктор, создающий счетчик и устанавливающий его значение в 0;
- __call__(self): магический метод, который позволяет использовать объект класса Counter как функцию, возвращающую текущее значение счетчика;
- increment(self): метод, увеличивающий значение счетчика на 1.
"""


class Counter:
    def __init__(self, value=0):
        self.__value = value

    def __call__(self):
        return self.__value

    def increment(self, value_to_add=1):
        self.__value += value_to_add


# код для проверки 
counter = Counter()
print(counter())  # 0

counter.increment()
print(counter())  # 1

counter.increment()
print(counter())  # 2
