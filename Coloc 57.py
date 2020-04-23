"""Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
Мельник Д.В. 122А
"""
rabotiagi = ['Каранський','Хоменко','Лобода','Березняк','Бартюк']  # Таблиця з робітниками
salary = [2300,3215,1815,2110,3635]  # Таблиця  з їх зарплатами
print(f'Робітники: {rabotiagi}')
print(f'Зарплати: {salary}')
universal_list = []  # наш список який ми будемо використовувати протягом всієї програми
summa = 0
for i in range(len(rabotiagi)):  # Шукаємо суму зарплат
    summa += salary[i]
average_salary = summa / len(rabotiagi)  # Середнє арифметичне
print(f'Середня зарплата {average_salary}')
for j in range(len(salary)):
    universal_list.append(abs(salary[j]-average_salary))  # віднімаємо зарплату від сер.зарплати і берем абсолютне знач, щоб побачити найменше відхилення
print(f'Різниця від середньої зарплати: {universal_list}')
for x in range(len(universal_list)):
    if universal_list[x] == min(universal_list):
        print(f'Прізвище працівника, зарплата якого найменш відхиляється від середньої зарплати: {rabotiagi[x]}')
universal_list.clear()  # Очищаємо наш ''Буфер''
for y in range(len(salary)):
    second_max = max(salary)-salary[y]  # Щоб визначити топ 2 по зарплаті потрібно від максимальної зарплати віднімати інші
    if second_max != 0:
        universal_list.append(second_max)  # Умова виконується доки ми не перейдемо до віднімання макс зарплати від самої себе
    if salary[y] == max(salary):
        print(f'Топ 1 по зарплаті: {rabotiagi[y]}')  # Виводим топ 1 по зарплаті
        break
    if len(universal_list) == len(salary)-1:
        for g in range(len(universal_list)):  # Перебираємо список зарплат(без топ 1) і знаходимо топ 2
            if universal_list[g] == min(universal_list):
                print(f'Топ 2 по зарплаті: {rabotiagi[g]}')
                break
for t in range(len(salary)):  # Проходимо по зарплатам і видаляємо відомості із списків
    if salary[t] == min(salary):
        del salary[t]
        del rabotiagi[t]
        break
print(f'Списки з видаленими відомостями про найменшу зарплату {rabotiagi}'
      f'{salary}')

