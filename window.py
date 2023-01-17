import main_2 as pp
from Otmetka import otmetka_prosmotra
while True:
    vvod_1 = input('Что хотите сделать? \n 1.Пометить просмотренное аниме. \n 2.Пометить брошенное аниме. \n 3.Получить рандомное аниме из спика "Буду смотреть". \n 4.Вывести список просмотренных аниме. \n 5.Вывести список "Буду смотреть" \n --Выход: qq \n ----> ')
    if vvod_1 == '1':
        pp.Print('later_po')
        num_element = int(input('Введите номер просмотренного аниме: '))
        otmetka_prosmotra(num_element, '+')
    elif vvod_1 == '2':
        pp.Print('later_po')
        num_element = int(input('Введите номер просмотренного аниме: '))
        otmetka_prosmotra(num_element, '-')    
    elif vvod_1 == '3':
        pp.Random_element()
    elif vvod_1 == '4':
        pp.Print('pros')
    elif vvod_1 == '5':
        pp.Print('later_po')
    elif vvod_1 == 'qq':
        break
    else:
        print("Вы ввели недопустимое число, пожалуйста будьте внимательнее! \n")
    