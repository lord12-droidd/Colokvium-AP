"""У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
Мельник Д.В. 122А
"""
# Тут місце у масиві буде слугувати нам квартирами
import random

people_in_flats = [random.randint(1,8) for i in range(30)]
people_in_flats_new = []
print(people_in_flats)
count = 0
for i in reversed(people_in_flats):  # Перевертаємо початковий список і йдем по кількості мешканців
    people_in_flats_new.append(i)  # Додаємо у наш пустий список
    if i > 5:
        count += 1
print(people_in_flats_new)  # Масив із новим розташуванням мешканців
print(f'Кількість квартир, в яких проживає більше 5 осіб: {count}')