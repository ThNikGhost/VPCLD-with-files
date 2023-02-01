'''Это модуль со всеми мною написанными функциями, которые были созданы для удобства и уменьшения кода.
Цель каждой функции - уменьшение количества строк кода.
Если какая-либо функция вам не понятна, пожалуйста напишите мне и я напишу их более подробное описание.
'''

def cut_counter_before_word(words: list) -> list:
    '''Отрезаем число перед элементом. Пример: ["1. Яблоко", "2. Апельсин"] --> ["Яблоко", "Апельсин"].
    Делаю, чтобы не получилось:
    >> 1. 1. Яблоко 
    Принимает words и возвращает его же, но без счёта в начале каждого элемента.
    '''
    empty_list = []
    if '.' in words[0]:
        for i in words:
            index = i.index('.')
            i = i[index+2:]
            empty_list.append(i)
        return empty_list
    else:
        return words

def create_dict_from_list(received_list: list) -> dict: 
    '''Создание словаря из списка.
    Принимает received_list(сам список).
    Возвращает dict_text словарь из этого списка. 
 
    Словарь нужен, чтобы проще было удалять нужный элемент с уникальным номером.
    '''
    len_dict = len(received_list)
    list_int = []
    dict_text = {}
    received_list = cut_counter_before_word(received_list)
    for i in range(1, len_dict+1):
        list_int.append(i)
    dict_text = dict(zip(list_int, received_list))
    if '\n' not in dict_text[len_dict]:
        dict_text[len_dict] = dict_text[len_dict] + '\n'
    return dict_text

def write_in_file(received_dict: dict, name_file, sort: bool = False) -> None:
    '''Запись словаря в файл, может отсортировать перед записью.
    Принимает received_dict(словарь), name_file(имя файла), sort(опционально, если надо True).
    '''
    if sort == True:
        received_dict = sort_dict(received_dict)
    for key,value in received_dict.items(): 
            text = ('{}{} {}'.format(key, '.', value))
            name_file.write(text)        

def print_data_from_file(name_file: str) -> None:
    '''Вывод информации из файла.
    Принимает имя файла(name_file).
    Выводит информацию из файла через функцию output_with_table.
    '''
    with open(f'text files/{name_file}.txt', 'r', encoding='UTF-8') as file:
        output_with_table(file.readlines())

def output_with_table(data: list | dict) -> None:
    '''Вывод данных в форме таблицы.
    Принимает список или словарь (data).
    Выводит информацию в виде таблицы.

    Используется в функции print_data_from_file.
    '''
    from rich.console import Console
    from rich.table import Table
    if type(data) == list:
        some_dict = create_dict_from_list(data)
    console = Console()
    table = Table(show_header=True, header_style="sky_blue3")
    table.add_column("[purple4]№")
    table.add_column("[medium_purple3]Title")
    for key, value in some_dict.items():
        table.add_row(
            f'[purple4]{key}', f'[medium_purple3]{value[:-1]}'
        )
    console.print(table)

def sort_dict(not_sort_dict: dict) -> dict:
    '''Сортировка словаря.
    Принимает словарь(received_dict).
    Возвращает отсортированный словарь(new_dict).
    '''
    list_values = list(not_sort_dict.values())
    list_values = sorted(list_values)
    new_dict = create_dict_from_list(list_values)
    return new_dict

def get_random_element() -> None:
    '''Получение рандомного элемента.
    Выводит рандомный элемент из файла "text files/planned.txt".
    '''
    import random
    from rich import print
    with open('text files/planned.txt', 'r', encoding='UTF-8') as file:
        text = random.choice(file.readlines())
        print(f'[purple4]{text}')

def move_element(path: str) -> None:
    '''Перенос элемента из одного файла в другой.
    Принимает имя файла(where) в который будет перенесён элемент.
    '''
    from rich import print
    print('[sky_blue2]Введите номер аниме: ', end='')
    num_element = int(input())
    with open('text files/planned.txt', 'r', encoding='UTF-8') as file:
        list_planned = file.readlines()
        dict_planned = create_dict_from_list(list_planned)
    with open(f'text files/{path}.txt', 'r', encoding='UTF-8') as file:
        list_file = file.readlines()
        dict_file = create_dict_from_list(list_file)
    name_file = f'{path}.txt'
    for key, value in list(dict_planned.items()):
        if key == num_element:
            del dict_planned[num_element]
            new_key = '*' + str(key)
            dict_file[new_key] = value
            print(f'[light_sky_blue3]Аниме [purple4]"{value[:-1]}"[light_sky_blue3] было перемещено в список [green]{name_file}')
            break
    # Открываются файлы уже в режиме записи, чтобы записать уже обновлённые списки
    with open('text files/planned.txt', 'w', encoding='UTF-8') as file:
        write_in_file(sort_dict(dict_planned), file, True)
    with open(f'text files/{path}.txt', 'w', encoding='UTF-8') as file:
        write_in_file(sort_dict(dict_file), file, True)
