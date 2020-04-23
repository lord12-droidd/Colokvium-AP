"""Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,20) for i in range(12)]
print(massive)
summa = 0
quantity = 0
for i in range(len(massive)):  # Проходим по елементам масиву
    if -2 <= massive[i] <= 10 :
        summa += massive[i]  # Шукаємо суму
        quantity += 1  # Додаємо до дільника +1
print(f'Cереднє значення елементів які потрапляють в інтервал від -2 до 10.: {summa/quantity}')