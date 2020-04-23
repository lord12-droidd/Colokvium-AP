"""Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(0,100) for i in range(12)]
print(massive)
summa = 0
quantity = 0
for i in range(len(massive)):  # Проходим по елементам масиву
    if massive[i] != min(massive):
        summa += massive[i]  # Шукаємо суму
        quantity += 1  # Додаємо до дільника +1
    if massive[i] == min(massive): # Якщо натрапляємо на мінімальний елемент то виходимо із циклу
        break
if summa == 0:
    print('Мінімальний елемент стоїть першим')
else:
    print(f'Cереднє значення елементів які розташовані за першим по порядку мінімальним елементом: {summa/quantity}')