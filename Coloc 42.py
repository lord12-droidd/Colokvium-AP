"""Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
Мельник Д.В. 122А
"""
import random
import math

count = 0
massive = [random.randint(4,110) for i in range(12)]
print(massive)
for i in range(len(massive)):  # Проходим по елементам масиву
    if i*i<massive[i] <math.factorial(i):  # Перевіряєм наші умови
        count += 1
print(f'Кількість елементів: {count}')