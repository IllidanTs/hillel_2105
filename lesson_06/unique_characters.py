input_characters = input("Введіть символи: ")
unique_characters = set(input_characters)
unique_count = len(unique_characters)
if unique_count > 10:
    print(True)
else:
    print(False)
