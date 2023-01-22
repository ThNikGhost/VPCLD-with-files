def otmetka_prosmotra(num_elemen: int, where: str):
    from Main import Create_dict, Write
    from main_2 import new_sort_dict
    from rich import print

    file_planned = open('text files/planned.txt', 'r', encoding='UTF-8')
    
    # В зависимости, от того, что выбрал пользователь, открывается нужный файл
    if where == 'completed':  
        file = open('text files/completed.txt', 'r', encoding='UTF-8')
        name_file = 'completed.txt'
    elif where == 'dropped':
        file = open('text files/dropped.txt', 'r', encoding='UTF-8')
        name_file = 'dropped.txt'
    elif where == 'liked':
        file = open('text files/liked.txt', 'r', encoding='UTF-8')
        name_file = 'liked.txt'
    
    list_planned = file_planned.readlines()  # Получаем строки из файла в виде списка
    list_file = file.readlines()  # Получаем строки из файла в виде списка

    # Преобразуем список в словарь с помощью функции Create_dict
    dict_file = Create_dict(len(list_file), list_file)
    dict_planned = Create_dict(len(list_planned), list_planned)

    for key, item in list(dict_planned.items()):
        # удаляем выбранный элемент из словаря dict_planned, а затем этот же элемент добавляем в dict_file
        if key == num_elemen:
            del dict_planned[num_elemen]
            new_key = '*' + str(key)
            dict_file[new_key] = item
            print(f'[light_sky_blue3]Аниме [purple4]"{item[:-1]}"[light_sky_blue3] было перемещено в список [green]{name_file}')
            break

    file_planned = open('text files/planned.txt', 'w', encoding='UTF-8')
    
    if where == 'completed':  # В зависимости, от того, что выбрал пользователь, открывается нужный файл
        file = open('text files/completed.txt', 'w', encoding='UTF-8')
    elif where == 'dropped':
        file = open('text files/dropped.txt', 'w', encoding='UTF-8')
    elif where == 'liked':
        file = open('text files/liked.txt', 'w', encoding='UTF-8')

    # записываем в файл planned.txt
    Write(new_sort_dict(dict_planned), file_planned, True)
    # записываем в файл completed.txt // dropped.txt
    Write(new_sort_dict(dict_file), file, True)

    file_planned.close()
    file.close()
