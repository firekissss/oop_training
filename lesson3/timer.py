"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from datetime import datetime


class Timer:
    def __enter__(self):
        self.time_start = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = datetime.now() - self.time_start


with Timer() as timer:
    for i in range(1000):
        pass

print("Execution time:", timer.elapsed_time)
