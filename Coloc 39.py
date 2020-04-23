"""Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Мельник Д.В. 122А
"""
import random

massive_temp = [random.randint(-10, 18) for i in range(10)]  # Створюємо масив генератором списку
print(f'Температури: {massive_temp}')
massive_opad = [random.randint(0, 200) for j in range(10)]  # Створюємо масив генератором списку
print(f'Опади:{massive_opad}')
summa_rain = 0
summa_snow = 0
for i in range(10):
    if massive_temp[i]>0:  # Якщо температура плюсова,то йшов дощ
        summa_rain += massive_opad[i]
    else:  # Якщо температура мінусова або 0, то йшов сніг
        summa_snow += massive_opad[i]
print(f'Кількість опадів, що випали у вигляді дощу: {summa_rain}')
print(f'Кількість опадів, що випали у вигляді снігу: {summa_snow}')
