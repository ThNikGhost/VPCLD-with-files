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


# Добавляет каждому элементу его число (Пример: 1. Название\n, 2. Название и т.д.)

"""def Sort(x, y):
    tuple_int = []
    tuple_str = []
    y = Srez(y)
    for n in range(1, x+1):
        tuple_int.append(n)  # создаём список с количеством элементов в полученном содержимом
    for d in range(0, x):
        stro = "{}{} {}".format(tuple_int[d], '.', y[d])
        tuple_str.append(stro)
    if '\n' not in tuple_str[x-1]:
        tuple_str[x-1] = tuple_str[x-1] + '\n'
    return tuple_str"""

# Создаём словарь ("х" - длина спика "у")
def Create_dict(x: int, y: list):  
    list_int = []
    dict_text = {}
    y = Srez(y)
    for i in range(1, x+1):
        list_int.append(i)
    dict_text = dict(zip(list_int, y))
    if '\n' not in dict_text[x]:
        dict_text[x] = dict_text[x] + '\n'
    return dict_text


'''
# Запись списка "x" в файл "у"
def Write(x: tuple, y):
    for i in x:
        y.write(i)    
'''
# Делаем из элементов словаря список, либо список из значений, либо список из ключей
def Get_list_from_dict(dict_:dict, what:str):
    new_list = []
    if what == 'key':
        for key, value in dict_.items():
            new_list.append(value) # Создаём список с значениями(value)
    elif what == 'value':
        for key, value in dict_.items():
            new_list.append(key)  # Создаём список с ключами(key)
    return new_list


# записываем данные словаря "х" в файл "у", Sort ответственнен за то, будет ли сортироваться список перед записью в файл
def Write(x: dict, y, sort: bool = False):
    if sort == True:
        from main_2 import new_sort_dict
        new_dict = new_sort_dict(x)
        for key,value in new_dict.items(): 
            text = ('{}{} {}'.format(key, '.', value))
            y.write(text)        
    elif sort == False:
        for key,value in x.items(): 
            text = ('{}{} {}'.format(key, '.', value))
            y.write(text)

    



'''
def later_po(x):
    file_po = open('Буду смотреть(по порядку).txt', x, encoding='UTF-8')
    return file_po

def later_ran(x):
    file_ra = open('Буду смотреть(рандом).txt', x, encoding='UTF-8')
    return file_ra

def pros_po(x):
    pros_sorted = open('Просмотренные(по порядку).txt', x, encoding='UTF-8')
    return pros_sorted
'''