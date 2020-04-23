"""Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.
Мельник Д.В. 122А
"""

massive = ['Melnyk','Molnyk','Molny','Melnykov','Melnykovskii']
for i in range(len(massive)):
    print(massive[-1 * (i + 1)])  # Використовуємо негативну індексацію для виводу навпаки
