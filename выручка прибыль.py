many_plus = float(input('Введите выручку: '))
many_min = float(input('Введите затраты: '))
result = many_plus - many_min
if result > 0:
    print(f'Ваша брибыль составила {result}! ')
    print(f'Рентабльность составляет {100 * result / many_plus:.1f}%')
    people = int(input('Введите коллиство сотрудников: '))
    print(f'Каждый сотрудник получит с прибыли по {result / people:.3f}.')
elif result < 0:
    print(f'Ваш убыток {-result}!')
else:
    print('Вы сработали в 0')
