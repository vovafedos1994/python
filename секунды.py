t_sek = int(input('Введите число в секундах: '))
hours = t_sek // 3600
min = t_sek // 60 - hours * 60
sek = t_sek % 60
time = (f'{hours:02}:{min:02}:{sek:02}')
print(time)
