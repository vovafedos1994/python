string = input('Введите строку из нескольких слов, раздленных пробелами: ').split()

for i, word in enumerate(string, 1):
     print(f'{i}. {word[:10]}')