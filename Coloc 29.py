"""Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
Мельник Д.В. 122А
"""
import random

a = int(input('Введіть ваше число: '))
massive = [random.randint(0,100) for i in range(12)]
print(massive)
quantity=0
for i in range(len(massive)):  # Перевіряємо на парність\непарність
    if massive[i]%2 == 0 and massive[i] != a:
        quantity += 1
    if massive[i] == a:  # Якщо число дорівнює заданому то припиняємо цикл
        break
print(f'Кількість парних елементів: {quantity}')