"""Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
Мельник Д.В. 122А
"""
import random

dry_months = []
dry_month = 0
massive = [random.randint(0,100) for i in range(12)]  # Генератор списку
print(massive)
summa = 0
for i in range(len(massive)):  # Проходим по елементам масиву
    summa += massive[i]  # Шукаємо суму
    if massive[i] < 30:  # Перевіряємо умову
        dry_months.append(massive[i])  # Якщо правдива то додаємо значення у пустий список
    if massive[i] == min(massive):  # Шукаємо найпосушливіший місяць
        dry_month = i
print(f'Загальна кількість опадів: {summa}')
print(f'Середньомісячна кількість опадів: {summa/12}')
print(f'Кількість посушливих місяців: {len(dry_months)}')
print(f'Найпосушливіший місяць року: {dry_month+1}')  # +1 щоб виводило номер місяця,а не індекс