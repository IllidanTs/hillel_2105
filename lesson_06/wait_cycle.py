while True:
    word = input("Введіть слово, яке містить літеру 'h': ")
    if 'h' in word.lower():
        print("Дякую, ви ввели правильне слово.")
        break
    else:
        print("Слово не містить літери 'h'. Спробуйте ще раз.")
