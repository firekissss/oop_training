"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return MyList2._Iterator(self.data)

    def __getitem__(self, index):
        return self.data[index]

    class _Iterator:
        def __init__(self, data):
            self._data = data
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self._data):
                raise StopIteration
            value = self._data[self._index]
            self._index += 1
            return value


# код для проверки
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print(my_list[1])  # 2
