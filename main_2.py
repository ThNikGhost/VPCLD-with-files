def Print(x: str): # упрощаю для себя вывод инфы с файла
    if x == 'completed':
        file = open('text files/completed.txt', 'r', encoding='UTF-8')
        Create_table_and_output(file.readlines())
        file.close()
    elif x == 'planned':
        file = open('text files/planned.txt', 'r', encoding='UTF-8')
        Create_table_and_output(file.readlines())
        file.close()
    elif x == 'liked':
        file = open('text files/liked.txt', 'r', encoding='UTF-8')
        Create_table_and_output(file.readlines())
        file.close()
    elif x == 'dropped':
        file = open('text files/dropped.txt', 'r', encoding='UTF-8')
        Create_table_and_output(file.readlines())
        file.close()

#Создание таблицы через библиотеку rich
def Create_table_and_output(list_: list):
    from rich.console import Console
    from rich.table import Table
    from Main import Create_dict
    dict_ = Create_dict(len(list_), list_)
    console = Console()
    table = Table(show_header=True, header_style="sky_blue3")
    table.add_column("[purple4]№")
    table.add_column("[medium_purple3]Title")
    for key, value in dict_.items():
        table.add_row(
            f'[purple4]{key}', f'[medium_purple3]{value[:-1]}'
        )
    console.print(table)

# Отрезаем число перед элементом. Пример: ["1. Яблоко", "2. Апельсин"] --> ["Яблоко", "Апельсин"]
def Srez(list: list):
    empty_list = []
    if '.' in list[0]:        
        for i in list:
            index = i.index('.')
            i = i[index+2:]
            empty_list.append(i)
        return empty_list
    else:
        return list

# Сортировать элемент с новым списком
def new_sort_list(x: list):
    x = Srez(x)
    x = sorted(x)
    return x

# сортирую словарь
def new_sort_dict(x: dict):
    from Main import Create_dict
    list_str = []
    for key, value in x.items():
        list_str.append(value)
    list_str = sorted(list_str)
    new_dict = Create_dict(len(list_str), list_str)
    return new_dict

# Выводит рандомный элемент из списка planned.txt
def Random_element():
    import random
    from rich import print
    file = open('text files/planned.txt', 'r', encoding='UTF-8')
    text = random.choice(file.readlines())
    print(f'[purple4]{text}')

# Добавляет элемент в файл
def func_check(str: str):
    from rich import print
    from Otmetka import otmetka_prosmotra
    print('[sky_blue2]Введите номер аниме: ', end='')
    num_element = int(input())
    otmetka_prosmotra(num_element, str)
