"""Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Мельник Д.В.
"""
import random

mult_massive = [] # Пустий масив для створення додавання туди помножених елементів
massive = [random.randint(1, 10) for i in range(7)]  # Генератор списку для ініцалізації масиву та його елементів
print(massive)
for i in massive:  # Цикл в якому ми проходимо по елементам масиву збільшуючи їх на 2
    mult_2 = i*2
    mult_massive.append(mult_2)  # Додаємо збільшений елемент у пустий масив
print(mult_massive)