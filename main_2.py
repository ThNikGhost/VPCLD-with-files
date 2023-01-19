def Print(x: str): # упрощаю для себя вывод инфы с файла
    if x == 'completed':
        file = open('text files/completed.txt', 'r', encoding='UTF-8')
        print(''.join(file.readlines()))
        file.close()
    elif x == 'planned':
        file = open('text files/planned.txt', 'r', encoding='UTF-8')
        print(''.join(file.readlines()))
        file.close()
    elif x == 'liked':
        file = open('text files/liked.txt', 'r', encoding='UTF-8')
        print(''.join(file.readlines()))
        file.close()
    elif x == 'dropped':
        file = open('text files/dropped.txt', 'r', encoding='UTF-8')
        print(''.join(file.readlines()))
        file.close()

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
    file = open('text files/planned.txt', 'r', encoding='UTF-8')
    print(random.choice(file.readlines()))

# Добавляет элемент в файл
def func_check(str: str):
    from Otmetka import otmetka_prosmotra
    try:
        num_element = int(input("Введите номер аниме: "))
        otmetka_prosmotra(num_element, str)
    except ValueError:
        print('Пожалуйста, будьте внимательнее, вы где-то допустили ошибку.')
    
#Спрашивать продолжить или закрыть программу


