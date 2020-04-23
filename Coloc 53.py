"""В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
Мельник Д.В. 122А
"""
import random


def selection_sort_ascending():
    for i in range(n - 1):
        min = i  # Припускаємо,що мінімум займає 'і' позицію
        for j in range(i + 1, n):
            if massive_x[j] < massive_x[min]:  # Порівнюємо чи елемент на 'j' позиціїї > елемент на 'min' позиції
                min = j  # Якщо умова правдива,то ми знайшли мінімальний елемент
        massive_x[i], massive_x[min] = massive_x[min], massive_x[i]
    print(f'{massive_x}')


n = int(input('Введіть число n: '))
massive_x = []  # Єдиний масив на всюо програму
while len(massive_x) <= n: # По суті увесь цей цикл рандомно заповнює масив
    massive_x.append(random.randint(0, 1))  # Додаємо в масив 1 або 0
    if len(massive_x) == n:
        break
    else:
        massive_x.append(5)  # Додаємо 5 якщо є місце
print(massive_x)
selection_sort_ascending()  # Викликаємо нашу функцію
