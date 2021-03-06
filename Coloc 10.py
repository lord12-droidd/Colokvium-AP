"""
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Мельник Д.В. 122А
"""
import random

dubak = 0
info_temp = [random.randint(-20, 15) for i in range(10)]  # Погода незрозуміла тому температура від -20 до 15, а декада це 10
print(info_temp)
for i in info_temp: # Проходимо по елементам масиву
    if i < -10:  # Якщо елемент менше -10 то кількість холодних днів +1
        dubak += 1
print(f'Число днів температури нижче -10 градусів: {dubak}')
