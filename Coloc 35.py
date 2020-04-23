"""35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
Мельник Д.В.122А
"""
import random

massive = [random.randint(-10, 10) for i in range(10)]  # Створюємо масив генератором списку
print(massive)
if massive == sorted(massive,reverse=True):  #Порівнюємо наш масив із відсортованим масивом по спаданню
    print('Відсортований')
else:
    print('Невідсортований')