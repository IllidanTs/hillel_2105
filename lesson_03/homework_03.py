alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Загальна площа Чорного та Азовського морів: {total_area} км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
items_first_second = 250449
items_second_third = 222950

items_second = items_first_second + items_second_third - total_items
items_first = items_first_second - items_second
items_third = items_second_third - items_second

print(f"Кількість товарів на першому складі: {items_first}")
print(f"Кількість товарів на другому складі: {items_second}")
print(f"Кількість товарів на третьому складі: {items_third}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
months = 18
total_cost = monthly_payment * months
print(f"Вартість комп'ютера: {total_cost} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

remainders = {
    '8019 % 8': 8019 % 8,
    '9907 % 9': 9907 % 9,
    '2789 % 5': 2789 % 5,
    '7248 % 6': 7248 % 6,
    '7128 % 5': 7128 % 5,
    '19224 % 9': 19224 % 9,
}

for expression, remainder in remainders.items():
    print(f"Остача від ділення {expression} = {remainder}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_large_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21

total_cost = (
    4 * pizza_large_price +
    2 * pizza_medium_price +
    4 * juice_price +
    cake_price +
    3 * water_price
)

print(f"Загальна вартість замовлення: {total_cost} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232
photos_per_page = 8
pages_needed = (total_photos + photos_per_page - 1) // photos_per_page
print(f"Кількість сторінок для вклеювання фотографій: {pages_needed}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance_km = 1600
fuel_per_100km = 9
tank_capacity = 48

total_fuel_needed = (distance_km / 100) * fuel_per_100km
print(f"Кількість літрів бензину, що знадобиться: {total_fuel_needed} л")

refuels_needed = (total_fuel_needed + tank_capacity - 1) // tank_capacity
print(f"Кількість заправок: {refuels_needed}")
