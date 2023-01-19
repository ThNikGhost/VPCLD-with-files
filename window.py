from main_2 import Print, Random_element, func_check
from Otmetka import otmetka_prosmotra
from rich import print
import os
co1 = 'sky_blue2' #цвет цифр '1.'
co2 = 'light_sky_blue3' #цвет текста 
Question = f'[{co1}]Что хотите сделать?'.center(50)
Question_2 = f'[{co1}]Какой список вывести?'.center(50)
while True:
    os.system('cls')
    Question = f'[{co1}]Что хотите сделать?'
    print(Question)
    print(f' [{co1}]1.[{co2}]Вывести списки. \n [{co1}]2.[{co2}]Пометить аниме как брошенное\просмотренное\любимое \n [{co1}]3.[{co2}]Другое \n --Выход: qq \n ----> ', end='')
    vvod = input()
    if vvod == '1':
        os.system('cls')
        print(Question_2)
        print(f' [{co1}]1.[{co2}]Запланированные аниме \n [{co1}]2.[{co2}]Просмотренные аниме. \n [{co1}]3.[{co2}]Брошенные аниме. \n [{co1}]4.[{co2}]Любимые аниме \n ----> ', end='')
        vvod_2 = input()        
        if vvod_2 == '1':
            Print('planned')
            print(f'[{co1}]Закрыть программу или продолжить? \n [{co1}]1.[{co2}]Закрыть. \n [{co1}]2.[{co2}]Продолжить. \n ----> ', end='')
            vvod_3 = input()
            if vvod_3 == '1':
                break
            elif vvod_3 == '2':
                continue
        elif vvod_2 == '2':
            Print('completed')
        elif vvod_2 == '3':
            Print('dropped')
        elif vvod_2 == '4':
            Print('liked')
    elif vvod == '2':
        os.system('cls')
        print(Question.center(50))
        print(f' [{co1}]1.[{co2}]Пометить брошенное аниме. \n [{co1}]2.[{co2}]Пометить просмотренное. \n [{co1}]3.[{co2}]Пометить любимое аниме. \n ----> ', end='')
        vvod_2 = input()
        if vvod_2 == '1':
            Print('planned')
            func_check('dropped')
        elif vvod_2 == '2':
            Print('planned')
            func_check('completed')        
        elif vvod_2 == '3':
            Print('planned')
            func_check('liked')
    elif vvod == '3':
        Random_element()
    elif vvod == 'qq':
        break