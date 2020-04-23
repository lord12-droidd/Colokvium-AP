"""Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-30,30) for i in range(20)]  # Ініціалізуємо масив
print(massive)
count = 0  # Лічильник
for i in range(20):
    count += massive.count(massive[i]) #Рахуємо входження елементу в масив(якщо елемент унікальний, то він буде додавати + 1 до лічильника)
if count == 20:  # Якщо кожен елемент унікальний,а елементів у нас 20, то значення лічильника буде 20
    print("Немає елементів з однаковими значеннями")
elif count > 20:  # Якщо ні, то лічильник буде більше 20
    print("Є елементи з однаковими значеннями")
