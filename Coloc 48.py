"""Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
Мельник Д.В. 122А
"""
# По суті це завдання це просто вивід списку в зворотньому порядку

n = int(input('Введіть брокера: '))  # К-сть брокерів
brokers = [input() for i in range(n)]
brokers_ch = []  # Пустий список для занесення
print(brokers)
for i in reversed(brokers):  # Перевертаємо початковий список і йдем по елементам
    brokers_ch.append(i)  # Додаємо елементи у наш пустий список
print(brokers_ch)
