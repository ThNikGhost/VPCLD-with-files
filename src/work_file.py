# Отрезаем число перед элементом. Пример: ["1. Яблоко", "2. Апельсин"] --> ["Яблоко", "Апельсин"]
# Делаю, чтобы не получилось >>> 1. 1. Яблоко <<< 
# То-есть, если надо добавить счёт, сначала убираю старый, а потом добавляю новый
def cutting_counter(received_list: list):
    empty_list = []
    if '.' in received_list[0]:        
        for i in received_list:
            index = i.index('.')
            i = i[index+2:]
            empty_list.append(i)
        return empty_list
    else:
        return received_list

# Создаём словарь ("х" - длина спика "у")
# Создаю словарь, чтобы в дальнейшем с работать с ним, а не с массивом
# Словарь нужен, чтобы проще было удалять нужный элемент с уникальным номером
# При работе с массивом, появляется баг, что удаляется не "1" элемент, а все элементы у которых в значении есть "1". 
def creating_dict(len_dict: int, received_list: list):  
    list_int = []
    dict_text = {}
    received_list = cutting_counter(received_list)
    for i in range(1, len_dict+1):
        list_int.append(i)
    dict_text = dict(zip(list_int, received_list))
    if '\n' not in dict_text[len_dict]:
        dict_text[len_dict] = dict_text[len_dict] + '\n'
    return dict_text

# записываем данные словаря "received_dict" в файл "name_file"
# Sort ответственнен за то, будет ли сортироваться словарь перед записью в файл
# Делаю запись в файл легче
def writing(received_dict: dict, name_file, sort: bool = False):
    if sort == True:
        received_dict = sorting_dict(received_dict)
    for key,value in received_dict.items(): 
            text = ('{}{} {}'.format(key, '.', value))
            name_file.write(text)        

# Делаю вывод информации из файла проще
def printing_data(text: str): 
    file = open(f'text files/{text}.txt', 'r', encoding='UTF-8')
    output_with_table(file.readlines())
    file.close()

# В этой функции происходит создание таблицы, с помощью библиотеки rich
# Далее таблица выводится на экран
# Используется в функции printing_data
def output_with_table(received_list: list):
    from rich.console import Console
    from rich.table import Table
    some_dict = creating_dict(len(received_list), received_list)
    console = Console()
    table = Table(show_header=True, header_style="sky_blue3")
    table.add_column("[purple4]№")
    table.add_column("[medium_purple3]Title")
    for key, value in some_dict.items():
        table.add_row(
            f'[purple4]{key}', f'[medium_purple3]{value[:-1]}'
        )
    console.print(table)

# Сортирую элементы в словаре
def sorting_dict(received_dict: dict):
    list_values = list(received_dict.values())
    list_values = sorted(list_values)
    new_dict = creating_dict(len(list_values), list_values)
    return new_dict

# Выводит рандомный элемент из файла 'text files/planned.txt'
def get_random_element():
    import random
    from rich import print
    file = open('text files/planned.txt', 'r', encoding='UTF-8')
    text = random.choice(file.readlines())
    print(f'[purple4]{text}')

# Переношу выбранный элемент в нужный файл 
def move_element(where: str):
    from rich import print
    print('[sky_blue2]Введите номер аниме: ', end='')
    # Объявление нужных переменных
    num_element = int(input())
    file_planned = open('text files/planned.txt', 'r', encoding='UTF-8')
    file = open(f'text files/{where}.txt', 'r', encoding='UTF-8')
    name_file = f'{where}.txt'
    list_planned = file_planned.readlines()  
    list_file = file.readlines()
    dict_file = creating_dict(len(list_file), list_file)
    dict_planned = creating_dict(len(list_planned), list_planned)
    # удаляем выбранный элемент из словаря dict_planned, а затем этот же элемент добавляем в dict_file
    for key, value in list(dict_planned.items()):
        if key == num_element:
            del dict_planned[num_element]
            new_key = '*' + str(key)
            dict_file[new_key] = value
            print(f'[light_sky_blue3]Аниме [purple4]"{value[:-1]}"[light_sky_blue3] было перемещено в список [green]{name_file}')
            break
    # Открываются файлы уже в режиме записи, чтобы записать уже обновлённые списки
    file_planned = open('text files/planned.txt', 'w', encoding='UTF-8')
    file = open(f'text files/{where}.txt', 'w', encoding='UTF-8')
    writing(sorting_dict(dict_planned), file_planned, True)
    writing(sorting_dict(dict_file), file, True)
    # Закрываю файлы
    file_planned.close()
    file.close()
