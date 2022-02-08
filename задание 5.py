my_list = [4, 5, 5, 7, 2]
new_num = int(input('Введите новый эдемент рейтинга(натуральное число): '))
n = 0
for i in my_list:
    if new_num <= i:
        n += 1
    else:
        break

my_list.insert(n, new_num)
print(my_list)