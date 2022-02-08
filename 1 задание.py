my_list = [1, 'beer', False, (77, 66), True, 15.7]
for i, item in enumerate(my_list, 1):
    print(f'{i}) {item} - {type(item)}')