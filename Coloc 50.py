"""У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
Мельник Д.В. 122А
"""
import random

tickets = []  # Тут зберігається 100 білетів
for i in range(100):
    tickets.append(i)  # Створюємо номери з 100 білетів
n = random.choice(tickets)  # Обираємо рандомно номер білета n
win_tickets = [random.randint(0,100) for i in range(10)]  # Створюємо виграшні номери
print(win_tickets)
win = False
for j in win_tickets:  # Я кщо номер нашого білета виграшний то виводимо це
    if j == n:
        print(f"Квиток виграшний, номер квитка був {n}")
        win = True
if win == False:
    print(f'Квиток невиграшний, номер квитка був {n}')
