days = 1
a_km = float(input('Начальный результат: '))
b_km = float(input('Конечный результат: '))
while a_km < b_km:
    a_km += a_km * 0.1
    days += 1

    print(f'Результат будет достигнут через {days} дней: ')
    break