""" Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Мельник Д.В. 122А
"""

massive = [int(input('Введіть елемент масиву: ')) for i in range(10)]  # Створюємо масив генератором списку
print(massive)
summa = 0
for i in range(10):
    if massive[i] > 0:
        summa += massive[i]
print(f'Cуму додатніх елементів: {summa}')
