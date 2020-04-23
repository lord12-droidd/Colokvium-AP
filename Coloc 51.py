"""Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,20) for i in range(12)]  # Ініціалізуємо масив
print(massive)
new_massive = []
for i in range(12):
    if massive[i] > i and massive[i]-i >= 10:  #Наш елемент повинен бути більше свого номера та перевищувати його на 10
        new_massive.append(massive[i])
if len(new_massive) != 0:
    print(new_massive)
else:
    print("Таких елементів немає")