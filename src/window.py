def window():
    from work_file import PrintingData, GetRandomElement, MoveElement
    from rich import print
    import os

    co1 = 'sky_blue2' #цвет цифр '1.' и вопросов
    co2 = 'light_sky_blue3' #цвет текста 

    while True:
        os.system('cls')
        print(f'[{co1}]Что хотите сделать?'.center(50))
        print(f' [{co1}]1.[{co2}]Вывести списки. \n [{co1}]2.[{co2}]Пометить аниме как брошенное\просмотренное\любимое \n [{co1}]3.[{co2}]Другое \n --Выход: qq \n ----> ', end='')
        vvod = input()
        if vvod == '1':
            os.system('cls')
            print(f'[{co1}]Какой список вывести?'.center(50))
            print(f' [{co1}]1.[{co2}]Запланированные аниме \n [{co1}]2.[{co2}]Просмотренные аниме. \n [{co1}]3.[{co2}]Брошенные аниме. \n [{co1}]4.[{co2}]Любимые аниме \n ----> ', end='')
            vvod_2 = input()        
            if vvod_2 == '1':
                PrintingData('planned') #Выводит planned.txt
            elif vvod_2 == '2':
                PrintingData('completed') #Выводит completed.txt
            elif vvod_2 == '3':
                PrintingData('dropped') #Выводит dropped.txt
            elif vvod_2 == '4':
                PrintingData('liked') #Выводит liked.txt
        elif vvod == '2':
            os.system('cls')
            print(f'[{co1}]Что хотите пометить?'.center(50))
            print(f' [{co1}]1.[{co2}]Пометить брошенное аниме. \n [{co1}]2.[{co2}]Пометить просмотренное. \n [{co1}]3.[{co2}]Пометить любимое аниме. \n ----> ', end='')
            vvod_2 = input()
            if vvod_2 == '1':
                PrintingData('planned') #Выводит planned.txt
                MoveElement('dropped') #Переносит нужное аниме в список dropped.txt
            elif vvod_2 == '2':
                PrintingData('planned')#Выводит planned.txt
                MoveElement('completed') #Переносит нужное аниме в список completed.txt        
            elif vvod_2 == '3':
                PrintingData('planned')#Выводит planned.txt
                MoveElement('liked') #Переносит нужное аниме в список liked.txt
        
        elif vvod == '3':
            os.system('cls')
            print(f'[{co1}]1.Вывести рандомное аниме. \n ---> ', end='')
            vvod_3 = input()
            if vvod_3 == '1':
                GetRandomElement()

        elif vvod == 'qq':
            break
        print(f'\n [{co1}]Закрыть программу или продолжить? \n [{co1}]1.[{co2}]Закрыть. \n [{co1}]2.[{co2}]Продолжить. \n ----> ', end='')
        vvod_3 = input()
        if vvod_3 == '1': break
