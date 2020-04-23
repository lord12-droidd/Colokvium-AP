"""Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,20) for i in range(12)]
a = int(input())
print(massive)
t = False
for i in range(len(massive)):  # Проходим по елементам масиву
    if max(massive) < a and massive.count(max(massive)) == 1:  # Перевіряєм наші умови
        t = True
print(f'Значення змінної t: {t}')
