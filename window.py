from main_2 import Print, Random_element, func_check
from Otmetka import otmetka_prosmotra
from rich import print
while True:
    Question = 'Что хотите сделать?'
    print(Question.center(50))
    vvod = input(' 1.Вывести списки. \n 2.Пометить аниме как брошенное\просмотренное\любимое \n 3.Другое \n --Выход: qq \n ----> ')
    if vvod == '1':
        print(Question.center(50))
        vvod_2 = input(' 1.Вывести список запланированных аниме \n 2.Вывести список просмотренных аниме. \n 3.Вывести список брошенных аниме. \n 4.Вывести список любимых аниме \n --Назад: .. \n ----> ')
        if vvod_2 == '1':
            Print('planned')
        elif vvod_2 == '2':
            Print('completed')
        elif vvod_2 == '3':
            Print('dropped')
        elif vvod_2 == '4':
            Print('liked')
        elif vvod_2 == '..':
            continue
    elif vvod == '2':
        print(Question.center(50))
        vvod_2 = input(' 1.Пометить брошенное аниме. \n 2.Пометить просмотренное. \n 3.Пометить любимое аниме. \n --Назад: .. \n ---->')
        if vvod_2 == '1':
            Print('planned')
            func_check('dropped')
        elif vvod_2 == '2':
            Print('planned')
            func_check('completed')        
        elif vvod_2 == '3':
            Print('planned')
            func_check('liked')
        elif vvod_2 == '..':
            continue
    elif vvod == '3':
        Random_element()
    elif vvod == 'qq':
        break