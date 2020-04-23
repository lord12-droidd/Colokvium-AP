"""У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
Мельник Д.В. 122А
"""
import random

massive = [random.randint(-10,20) for i in range(12)]  # Ініціалізуємо масив
print(massive)
for i in range(12):
    if i == 0 and massive[i]== max(massive):  # Якщо максимальний елемент масиву найперший то ставимо 0 на 0 позицію
        massive.insert(0,0)
    elif massive[i] == max(massive):  # Якщо знайшли максимальний елемент,то беремо його індекс і вставляємл на позицію
        massive.insert(i,i)  # його ідексу
        break  # можна перервати цикл щоб програма робила це лише з одним максимальним елеменентом
print(massive)
