'''Главный модуль.
Эта функция отвечает за меню программы.
'''
import work_file as w
from rich import print
import os

def window():
    digit_color = 'sky_blue2' #также цвет вопросов
    text_color = 'light_sky_blue3' 
    while True:
        os.system('cls')
        print(f'[{digit_color}]Что хотите сделать?'.center(50))
        print(f"""[{digit_color}]1.[{text_color}]Вывести списки.  \
                  \n[{digit_color}]2.[{text_color}]Пометить аниме как брошенное\просмотренное\любимое.  \
                  \n[{digit_color}]3.[{text_color}]Другое  \
                  \n--Выход: qq  \
                  \n----> """, end='')
        entry = input()
        if entry == '1': # Вывод меню, где пользователь выбирает, какой список он хочет вывести
            os.system('cls')
            print(f'[{digit_color}]Какой список вывести?'.center(50))
            print(f"""[{digit_color}]1.[{text_color}]Запланированные аниме.  \
                      \n[{digit_color}]2.[{text_color}]Просмотренные аниме.  \
                      \n[{digit_color}]3.[{text_color}]Брошенные аниме.  \
                      \n[{digit_color}]4.[{text_color}]Любимые аниме.  \
                      \n----> """, end='')
            entry_2 = input()
            if entry_2 != '': 
                dict_entry = {1: 'planned', 2: 'completed', 3: 'dropped', 4: 'liked'}
                w.print_data_from_file(dict_entry[int(entry_2)])
        elif entry == '2': # Вывод меню, где пользователь выбирает, что он хочет пометить
            os.system('cls')
            print(f'[{digit_color}]Что хотите пометить?'.center(50))
            print(f"""[{digit_color}]1.[{text_color}]Пометить брошенное аниме.  \
                      \n[{digit_color}]2.[{text_color}]Пометить просмотренное.  \
                      \n[{digit_color}]3.[{text_color}]Пометить любимое аниме.  \
                      \n----> """, end='')
            entry_2 = input()
            if entry_2 != '':
                w.print_data_from_file('planned')
                dict_entry = {1: 'dropped', 2: 'completed', 3: 'liked'}
                w.move_element(dict_entry[int(entry_2)])
        elif entry == '3': # Вывод рандомного элемента
            os.system('cls')
            print(f'[{digit_color}]1.Вывести рандомное аниме. \n ---> ', end='')
            entry_3 = input()
            if entry_3 == '1':
                w.get_random_element()
        elif entry == 'qq': break
        print(f"""[{digit_color}]Закрыть программу или продолжить?  \
                  \n[{digit_color}]1.[{text_color}]Закрыть.  \
                  \n[{digit_color}]2.[{text_color}]Продолжить.  \
                  \n----> """, end='')
        entry_3 = input()
        if entry_3 == '1': break

if __name__ == '__main__':
    window()