"""Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Мельник Д.В. 122А
"""
import random

cratni = []
massive = [random.randint(10, 100) for i in range(10)]  # Створюємо масив генератором списку
print(massive)
mult = 1
for i in massive:  # Проходим по елементам масиву
    if i % 5 == 0:  # Перевіряємо нашу умову
        mult *= i  # Шукаємо добуток таких чисел
        cratni.append(i)
if len(cratni) == 0:
    print('Немає елементів масиву, кратних 5')
elif len(cratni) >= 1:
    print(f'добуток елементів масиву, кратних 5: {mult}')