name = input('Привет,как тебя зовут: ')
print(name)

location = input(f'Очень приятно {name}! А где ты живешь?: ')
print(location)

age = input(f'Круто! {name}, а сколько тебе лет?: ')
print(age)

program = input(f'Отличо! ,{name}, хочешь начать изучать программирование?(ответь да или нет) :')
if program == 'да':
    print('Прекрасно! Ты сделал правильный выбор')

if program == 'нет':
    print('Тогда ты не по адресу')