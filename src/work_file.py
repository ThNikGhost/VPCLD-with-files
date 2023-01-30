'''Это модуль со всеми мною написанными функциями, которые были созданы для удобства и уменьшения кода
Цель каждой функции - облегчение написания кода
Если какая-либо функция вам не понятна, пожалуйста напишите мне и я напишу их более подробное описание
'''

def cutting_counter(received_list: list):
    '''Отрезаем число перед элементом. Пример: ["1. Яблоко", "2. Апельсин"] --> ["Яблоко", "Апельсин"]
    Делаю, чтобы не получилось:
    >> 1. 1. Яблоко 
    Принимает received_list и возвращает его же, но без счёта в начале каждого элемента
    '''
    empty_list = []
    if '.' in received_list[0]:        
        for i in received_list:
            index = i.index('.')
            i = i[index+2:]
            empty_list.append(i)
        return empty_list
    else:
        return received_list

def creating_dict(received_list: list):
    '''Создание словаря из списка
    Принимает received_list(сам список)
    Возвращает dict_text словарь из этого списка 
 
    Словарь нужен, чтобы проще было удалять нужный элемент с уникальным номером
    '''
    len_dict = len(received_list)
    list_int = []
    dict_text = {}
    received_list = cutting_counter(received_list)
    for i in range(1, len_dict+1):
        list_int.append(i)
    dict_text = dict(zip(list_int, received_list))
    if '\n' not in dict_text[len_dict]:
        dict_text[len_dict] = dict_text[len_dict] + '\n'
    return dict_text

def writing(received_dict: dict, name_file, sort: bool = False):
    '''Запись словаря в файл, может отсортировать перед записью
    Принимает received_dict(словарь), name_file(имя файла), sort(опционально, если надо True)
    '''
    if sort == True:
        received_dict = sorting_dict(received_dict)
    for key,value in received_dict.items(): 
            text = ('{}{} {}'.format(key, '.', value))
            name_file.write(text)        

def printing_data(name_file: str):
    '''Вывод информации из файла
    Принимает имя файла(name_file)
    Ничего не возвращает, выводит информацию из файла через функцию output_with_table
    '''
    with open(f'text files/{name_file}.txt', 'r', encoding='UTF-8') as file:
        output_with_table(file.readlines())

def output_with_table(received: list | dict):
    '''Вывод данных в форме таблицы
    Принимает список или словарь (received)
    Ничего не возвращает, выводит информацию в виде таблицы

    Используется в функции printing_data
    '''
    from rich.console import Console
    from rich.table import Table
    if type(received) == list:
        some_dict = creating_dict(received)
    console = Console()
    table = Table(show_header=True, header_style="sky_blue3")
    table.add_column("[purple4]№")
    table.add_column("[medium_purple3]Title")
    for key, value in some_dict.items():
        table.add_row(
            f'[purple4]{key}', f'[medium_purple3]{value[:-1]}'
        )
    console.print(table)

def sorting_dict(received_dict: dict):
    '''Сортировка словаря
    Принимает словарь(received_dict)
    Возвращает отсортированный словарь(new_dict)
    '''
    list_values = list(received_dict.values())
    list_values = sorted(list_values)
    new_dict = creating_dict(list_values)
    return new_dict

def get_random_element():
    '''Получение рандомного элемента
    Ничего не принимает
    Возвращает рандомный элемент из файла "text files/planned.txt"
    '''
    import random
    from rich import print
    with open('text files/planned.txt', 'r', encoding='UTF-8') as file:
        text = random.choice(file.readlines())
        print(f'[purple4]{text}')

def move_element(where: str):
    '''Перенос элемента из одного файла в другой
    Принимает имя файла(where) в который будет перенесён элемент
    Ничего не возвращает
    '''
    from rich import print
    print('[sky_blue2]Введите номер аниме: ', end='')
    # Объявление нужных переменных
    num_element = int(input())
    with open('text files/planned.txt', 'r', encoding='UTF-8') as file:
        list_planned = file.readlines()
        dict_planned = creating_dict(list_planned)
    with open(f'text files/{where}.txt', 'r', encoding='UTF-8') as file:
        list_file = file.readlines()
        dict_file = creating_dict(list_file)
    name_file = f'{where}.txt'
    for key, value in list(dict_planned.items()):
        if key == num_element:
            del dict_planned[num_element]
            new_key = '*' + str(key)
            dict_file[new_key] = value
            print(f'[light_sky_blue3]Аниме [purple4]"{value[:-1]}"[light_sky_blue3] было перемещено в список [green]{name_file}')
            break
    # Открываются файлы уже в режиме записи, чтобы записать уже обновлённые списки
    with open('text files/planned.txt', 'w', encoding='UTF-8') as file:
        writing(sorting_dict(dict_planned), file, True)
    with open(f'text files/{where}.txt', 'w', encoding='UTF-8') as file:
        writing(sorting_dict(dict_file), file, True)
