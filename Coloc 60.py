"""Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(1,8) for i in range(10)]   # Створюємо масив генератором списку
count_list = []
print(massive)
count = 0
for i in range(len(massive)):
    if i == len(massive)-2 and count == 1 and massive[i] == massive[-1]: # Якщо дійшли до передостаннього елементу і вже був 1 збіг, то порівнюємо його з останнім
        print(f'Значення змінної: ')
        break
    elif count != 1 and massive[i] == massive[-1] and i == len(massive)-1:  # Якщо останній елемент і до того збігів не було то точно збігу далі не буде False
        print(f'Значення змінної: ')
        break
    elif count == 1 and massive[i] == massive[-1] and i == len(massive)-1:  # Якщо останній елемент і збіг був то далі немає з чим порівнювати,тому теж False
        print(f'Значення змінної:')
        break
    if massive[i] == massive[i+1] and count >= 2:  # Перевіряємо умову
        count += 1  # Додаємо +1 до лічильника
        count_list.append(count)
    elif massive[i] == massive[i+1]:  # Перевіряємо умову
        count += 2  # Якщо елементи співпадають вперше,то додаємо +2 до лічильника
        count_list.append(count)
    else:
        count = 0
try:
    print(max(count_list))  # Якщо список з кількістю значень що ідуть підряд буде пустий,то буде помилка,яку ми перехвачуєм
except ValueError:
    print('Немає чисел що йдуть підряд')