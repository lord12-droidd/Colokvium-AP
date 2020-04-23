"""Розсортуйте заданий лінійний масив по зростанню.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10, 10) for i in range(10)]  # Створюємо масив генератором списку
print(massive)
print(sorted(massive))  # Сортуємо
