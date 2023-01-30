def window():
    from work_file import printing_data, get_random_element, move_element
    from rich import print
    import os

    co1 = 'sky_blue2' #цвет цифр '1.' и вопросов
    co2 = 'light_sky_blue3' #цвет текста 
    while True:
        os.system('cls')
        print(f'[{co1}]Что хотите сделать?'.center(50))
        print(f"""[{co1}]1.[{co2}]Вывести списки.  \
                  \n[{co1}]2.[{co2}]Пометить аниме как брошенное\просмотренное\любимое  \
                  \n[{co1}]3.[{co2}]Другое  \
                  \n--Выход: qq  \
                  \n----> """, end='')
        entry = input()
        if entry == '1': # Вывод меню, где пользователь выбирает, какой список он хочет вывести
            os.system('cls')
            print(f'[{co1}]Какой список вывести?'.center(50))
            print(f"""[{co1}]1.[{co2}]Запланированные аниме  \
                      \n[{co1}]2.[{co2}]Просмотренные аниме.  \
                      \n[{co1}]3.[{co2}]Брошенные аниме.  \
                      \n[{co1}]4.[{co2}]Любимые аниме  \
                      \n----> """, end='')
            entry_2 = input()
            if entry_2 != '': 
                dict_entry = {1: 'planned', 2: 'completed', 3: 'dropped', 4: 'liked'}
                printing_data(dict_entry[int(entry_2)])
        elif entry == '2': # Вывод меню, где пользователь выбирает, что он хочет пометить
            os.system('cls')
            print(f'[{co1}]Что хотите пометить?'.center(50))
            print(f"""[{co1}]1.[{co2}]Пометить брошенное аниме.  \
                      \n[{co1}]2.[{co2}]Пометить просмотренное.  \
                      \n[{co1}]3.[{co2}]Пометить любимое аниме.  \
                      \n----> """, end='')
            entry_2 = input()
            if entry_2 != '':
                printing_data('planned')
                dict_entry = {1: 'dropped', 2: 'completed', 3: 'liked'}
                move_element(dict_entry[int(entry_2)])
        elif entry == '3': # Вывод рандомного элемента
            os.system('cls')
            print(f'[{co1}]1.Вывести рандомное аниме. \n ---> ', end='')
            entry_3 = input()
            if entry_3 == '1':
                get_random_element()
        elif entry == 'qq': break
        print(f"""[{co1}]Закрыть программу или продолжить?  \
                  \n[{co1}]1.[{co2}]Закрыть.  \
                  \n[{co1}]2.[{co2}]Продолжить.  \
                  \n----> """, end='')
        entry_3 = input()
        if entry_3 == '1': break