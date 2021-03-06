"""
Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-15, 30) for i in range(15)]  # Генератор списку для ініцалізації масиву та його елементів
print(massive)
print(max(massive))  # Використовуємо метод max для знаходження найбцльшого елементу
for i in range(len(massive)):
    if massive[i] == max(massive):  # Звертаємось по індексу щоб порівнювати елемент списку з максимальним елементом
        print(f'Максимальний елемент має індекс {i}')  # Якщо умова спрацьовує то виводимо на екран ІНДЕКС елементу
        # Якщо елементів декілька то виводимо відповідні для них ІНДЕКСИ
