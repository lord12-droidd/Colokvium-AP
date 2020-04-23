"""
Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,20) for i in range(12)]  # Ініціалізуємо масив
print(massive)
new_massive = []
for i in range(12):
    if massive[i] % 2 == 0 and i % 2 == 0:  # Перевіряємо умову
        new_massive.append(massive[i])
count = new_massive.count(max(new_massive))  # Рахуємо скільки у нас елементів у спиcку
if count == 1:
    print("Елемент єдиний")
elif count > 1:
    print("Такий елемент не єдиний")
else:
    print("Таких елементів немає")
