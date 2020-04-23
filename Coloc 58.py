"""Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(1,8) for i in range(15)]  # Створюємо масив генератором списку
print(massive)

max_count = 0
count_list = []
for i in range(len(massive)):
    n = massive.count(massive[i])  # Рахуємо скільки разів повторюються кожне число
    count_list.append(n)  # Додаємо кільсть повторів у пустий список
    if count_list[i] == max(count_list):
        max_count = count_list[i]  # Проходимо по списку шукаємо максимальну кільсть повторів
print(f'К-сть повторів найчастішого числа: {max_count}')