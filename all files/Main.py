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
