"""Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
Мельник Д.В. 122А
"""

import random

massive_a = [random.randint(-10, 10) for i in range(10)]  # Створюємо масив генератором списку
print(f'Перший масив: {massive_a}')
massive_b = [random.randint(-12, 12) for j in range(10)]  # Створюємо масив генератором списку
print(f'Другий масив:{massive_b}')
massive_c = []
for x in range(len(massive_a)):
    massive_c.append(massive_a[x]*massive_b[x])  # Множимо відповідні елементи масивів
print(f'Результат  : {massive_c}')
