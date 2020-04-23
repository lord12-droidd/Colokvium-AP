"""Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(200, 300) for i in range(20)]  # Створюємо масив генератором списку
print(massive)
summa = 0
for i in massive:  # Проходим по елементам масиву
    if i % 2 == 3:  # Перевіряємо нашу умову
        summa += i  # Шукаємо суму таких чисел(буде завжди сума 0,бо для парних остача 0,а для непарних 1)
print(f'Cума парних елементів масиву: {summa}')