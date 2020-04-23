"""Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Мельник Д.В. 122А
"""

import random

massive = [random.randint(150, 300) for i in range(20)] #
print(massive)
summa = 0
summa_lower_average = 0
lower_average = 0  # Наш лічильник
for i in range(len(massive)):   # Сума елементів масиву
    summa += massive[i]
average = summa / len(massive)  #Середнє арифметичне
for j in massive:
    if j < average:  # Якщо елемент менше середнього арифметичного
        summa_lower_average += j  # То додаємо його у суму таких самих елементів
print(f'Середнє арифметичне {average}')
print(f'Cума всіх елементів масиву, які менше середнього арифметичного елементів масиву: {summa_lower_average}')