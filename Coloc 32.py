"""Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,20) for i in range(12)]
print(massive)
t = False
for i in range(len(massive)):  # Проходим по елементам масиву
    if massive[i]<0 and massive[i] % 2 == 0:
        t = True
print(f'Значення змінної t: {t}')
