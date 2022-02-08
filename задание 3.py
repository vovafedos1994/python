seasons = {'Зима': [12, 1, 2], 'Лето': [6, 7,8], 'Осень': [9, 10, 11]}

num_month = int(input('Введите цифрой номер месяца: ' ))

if num_month in sum(seasons.values(), []):
    for i in seasons.items():
        if num_month in i[1]:
            print(i[0])
            break