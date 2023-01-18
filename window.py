import main_2 as pp
from Otmetka import otmetka_prosmotra
while True:
    Question = 'Что хотите сделать?'
    print(Question.center(50))
    vvod_1 = input(' 1.Пометить просмотреное аниме. \n 2.Пометить брошеное аниме. \n 3.Получить рандомное аниме из спика "Буду смотреть". \n 4.Вывести список просмотренных аниме. \n 5.Вывести список "Буду смотреть". \n 6.Добавить аниме в Любимое. \n --Выход: qq \n ----> ')
    if vvod_1 == '1':
        pp.Print('planned')
        try:
            num_element = int(input('Введите номер просмотренного аниме: '))
            otmetka_prosmotra(num_element, 'completed')
        except ValueError:
            print('Пожалуйста, будьте внимательнее, вы где-то ошиблись.')    
    elif vvod_1 == '2':
        pp.Print('planned')
        try:
            num_element = int(input('Введите номер заброшенного  аниме: '))
            otmetka_prosmotra(num_element, 'dropped')
        except ValueError:
            print('Пожалуйста, будьте внимательнее, вы где-то ошиблись.')    
    elif vvod_1 == '3':
        pp.Random_element()
    elif vvod_1 == '4':
        pp.Print('completed')
    elif vvod_1 == '5':
        pp.Print('planned')
    elif vvod_1 == '6':
        pp.Print('planned')
        num_element = int(input('Введите номер понравившегося аниме: '))
        otmetka_prosmotra(num_element, 'liked')
    elif vvod_1 == 'qq':
        break
    else:
        print("Вы ввели недопустимое число, пожалуйста будьте внимательнее! \n")
    