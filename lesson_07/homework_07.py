# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(3, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2, 3, 4, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key=len)
print(longest_word(["apple", "banana", "cherry"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7 ?
# task 8 ?
# task 9 ?

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
def filter_strings_from_list(lst):
    return [item for item in lst if isinstance(item, str)]
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(filter_strings_from_list(lst1))

def unique_characters_count(input_characters):
    unique_characters = set(input_characters)
    unique_count = len(unique_characters)
    return unique_count > 10
print(unique_characters_count("abcdefgABCDEFG"))
print(unique_characters_count("abcde"))

def sum_of_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_even_numbers(numbers))

def wait_for_word_with_h():
    while True:
        word = input("Введіть слово, яке містить літеру 'h': ")
        if 'h' in word.lower():
            print("Дякую, ви ввели правильне слово.")
            return word
        else:
            print("Слово не містить літери 'h'. Спробуйте ще раз.")