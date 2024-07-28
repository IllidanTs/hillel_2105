# Генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(N):
    for number in range(0, N + 1, 2):
        yield number

print("Генератор парних чисел від 0 до N:")
N = 10
for num in even_numbers(N):
    print(num)

# Генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

print("\nГенератор послідовності Фібоначчі до N:")
N = 50
for num in fibonacci(N):
    print(num)

# Ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

print("\nІтератор для зворотного виведення елементів списку:")
my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)

# Ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.N:
            raise StopIteration
        return self.current

print("\nІтератор для парних чисел в діапазоні від 0 до N:")
N = 10
for num in EvenIterator(N):
    print(num)

# Декоратор, який логує аргументи та результати викликаної функції.
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Arguments: {args}, {kwargs}")
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print("\nДекоратор, який логує аргументи та результати функції:")
add(2, 3)

# Декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print("\nДекоратор, який перехоплює та обробляє винятки:")
divide(10, 0)

