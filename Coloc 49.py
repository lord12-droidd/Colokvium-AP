"""Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
Мельник Д.В. 122А
"""
servises = ['Готовка','Уборка','Патрульвання','Водіння','Навчання','Тренування']
price = [210,320,300,100,340,250]
g = int(input('Введіть ціну: '))  #Вводимо ціну послуги
for i in range(len(servises)):
    if price[i] == g:  # У нас накопичена змінна і (стільки разів ми будемо видаляти елементи далі)
        for j in range(i):
            del servises[0]  # Видаляємо перші елементи списків до тих пір поки не наткнемся на введену ціну
            del price[0]
        break  # Все зробили тому виходимо із циклу
print(servises)
print(price)
