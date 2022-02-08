list_enter = input('Введите числа списка через пробел - ').split()

for i in range(1, len(list_enter), 2):
    list_enter.inser(i - 1, list_enter.pop(i))

print(list_enter)
