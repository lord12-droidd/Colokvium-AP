"""Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
Мельник Д.В. 122А
"""
# Порівнюю поточний елемент з наступним тому так багато іфів(щоб програма не вилітала)
import random

massive = [random.randint(1,8) for i in range(15)]  # Створюємо масив генератором списку
print(massive)
count = 0
r = False
for i in range(len(massive)):
    if i == len(massive)-2 and count == 1 and massive[i] == massive[-1]: # Якщо дійшли до передостаннього елементу і вже був 1 збіг, то порівнюємо його з останнім
        r = True
        print(f'Значення змінної: {r}')
        break
    elif count != 1 and massive[i] == massive[-1] and i == len(massive)-1:  # Якщо останній елемент і до того збігів не було то точно збігу далі не буде False
        print(f'Значення змінної: {r}')
        break
    elif count == 1 and massive[i] == massive[-1] and i == len(massive)-1:  # Якщо останній елемент і збіг був то далі немає з чим порівнювати,тому теж False
        print(f'Значення змінної: {r}')
        break
    if massive[i] == massive[i+1]:  # Перевіряємо умову
        count += 1  # Додаємо +1 до лічильника
        if count >= 2:
            r = True
            print(f'Значення змінної: {r}')
            break
    else:
        count = 0