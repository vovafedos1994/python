num_user = int(input('Введите любое целое подожитльное число: '))
num_per = 0
while num_user != 0:
    fin_num = num_user % 10
    if fin_num > 0:
        num_per = fin_num
        if fin_num == 9:
            break
    num_user //= 10

print(f'Наибольшая цифра в вашем числе {fin_num}')

    