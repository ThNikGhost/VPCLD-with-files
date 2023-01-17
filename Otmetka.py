def otmetka_prosmotra(num_elemen: int, where: str):
    from Main import Create_dict, Write
    from main_2 import new_sort_dict
    later_po = open('text files/planned.txt', 'r', encoding='UTF-8')
    if where == '+':  # В зависимости, от того, что выбрал пользователь, открывается нужный файл
        pros_po = open('text files/completed.txt', 'r', encoding='UTF-8')
        name_file = 'completed.txt'
    elif where == '-':
        pros_po = open('text files/dropped.txt', 'r', encoding='UTF-8')
        name_file = 'dropped.txt'
    list_later = later_po.readlines()  # Получаем строки из файла в виде списка
    list_pros = pros_po.readlines()  # Получаем строки из файла в виде списка
    # Преобразуем список в словарь с помощью функции Create_dict
    dict_pros = Create_dict(len(list_pros), list_pros)
    # Преобразуем список в словарь с помощью функции Create_dict
    dict_later = Create_dict(len(list_later), list_later)
    for key, item in list(dict_later.items()):
        # удаляем выбранный элемент из словаря dict_later, а затем этот же элемент добавляем в dict_pros
        if key == num_elemen:
            del dict_later[num_elemen]
            new_key = '*' + str(key)
            dict_pros[new_key] = item
            print(f'Аниме "{item[:-1]}" было перемещено в список {name_file}')
            break
    """
    for i in list_later:
        if num_element in i[:3]:
            list_later.remove(i)
            list_pros.append(i)
    """
    later_po = open('text files/planned.txt', 'w', encoding='UTF-8')
    if where == '+':  # В зависимости, от того, что выбрал пользователь, открывается нужный файл
        pros_po = open('text files/completed.txt', 'w', encoding='UTF-8')
    elif where == '-':
        pros_po = open('text files/dropped.txt', 'w', encoding='UTF-8')

    # записываем в файл planned.txt
    Write(new_sort_dict(dict_later), later_po, True)
    # записываем в файл completed.txt // dropped.txt
    Write(new_sort_dict(dict_pros), pros_po, True)

    later_po.close()
    pros_po.close()
