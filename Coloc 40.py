"""Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,10) for i in range(20)]
print(massive)
summa = 0
for i in range(len(massive)):  # Проходим по елементам масиву
    if massive[i] % 2 == 0 and massive[i] != 0:
        summa += massive[i]  # Шукаємо суму
    elif massive[i] == 0:  # Якщо натикаємось на 0 , то прериваємо ітерації
        break
print(f'Cума парних елементів масиву до першого зустрінутого нульового елемента: {summa}')