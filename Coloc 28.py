"""Знайти кількість парних елементів одновимірного масиву.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(0,100) for i in range(12)]
print(massive)
quantity=0
for i in range(len(massive)):  # Перевіряємо на парність\непарність
    if massive[i]%2==0:
        quantity += 1
print(f'Кількість парних елементів: {quantity}')