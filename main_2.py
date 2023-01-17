def Print(x: str): # упрощаю для себя вывод инфы с файла
    if x == 'pros':
        pros = open('Просмотренные(по порядку).txt', 'r', encoding='UTF-8')
        print(''.join(pros.readlines()))
    elif x == 'later_po':
        later_po = open('Буду смотреть(по порядку).txt', 'r', encoding='UTF-8')
        print(''.join(later_po.readlines()))
    elif x == 'later_ra':
        later_ra = open('Буду смотреть(рандом).txt', 'r', encoding='UTF-8')
        print(''.join(later_ra.readlines()))

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

# Выводит рандомный элемент из списка Буду смотреть(по порядку).txt
def Random_element():
    import random
    file = open('Буду смотреть(по порядку).txt', 'r', encoding='UTF-8')
    print(random.choice(file.readlines()))
