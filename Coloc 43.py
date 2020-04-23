"""Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b."""
import random

a = 0
b = 0
while a<=0 or b<=0:  # Перевірка на натуральність числа
    a = int(input('Введіть натуральне число А:'))
    b = int(input('Введіть натуральне число В:'))
massive = [random.randint(-10,20) for i in range(12)]  # Створюємо масив
print(massive)
w = False
for i in range(len(massive)):
    if massive[i]%a == 0 and massive[i]%b != 0:  # Перевіряєсо нашу умову
        w = True
print(f'Значення змінної w: {w}')
