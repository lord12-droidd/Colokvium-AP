"""
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Мельник Д.В. 122А
"""
import random

info_temp = [random.randint(-15, 15) for i in range(10)] # Погода незрозуміла тому температура від -15 до 15, а декада це 10
print(info_temp)
summa = 0
higher_average = 0  # Наш лічильник
for i in range(len(info_temp)):   # Сума елементів масиву
    summa += info_temp[i]
average = summa / len(info_temp)  #Середнє арифметичне
for j in info_temp:
    if j > average:  # Якщо поточна температура дня вища за середню декади
        higher_average += 1  # Додаємо до лічильника +1
print(f'Середнє арифметичне {summa/10}')
print(f'Кількість днів температури вище середньої: {higher_average}')
