"""Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
Мельник Д.В. 122А
"""
import numpy as np

import random

count = 0
a = np.zeros((4,10),dtype = int)  # Можна представити дані у вигляді масиву із 4 рядками(напрямками) і 10 стовпцями(днями)
for i in range(4):  # За 1 день вітер може дути у декілька напрямків тому елементів масиву буде 40
    for j in range(10):
        a[i,j] = random.randint(0,15)  # Створюємо елементи масиву які відповідають за силу вітру
for x in range(10):
    if a[1,x]>8:  # Якщо у другому рядку(він відповідає за південний напрям,згідно умови) є елемент >8 то додаємо у лічильник 1
        count += 1
print(a)
print(count)  # Виводимо кількість днів у яких вітер був сильніше за 8 м\с
