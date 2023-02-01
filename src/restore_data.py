'''Технический модуль, для теста, чтобы быстро восстанавливать данные в файлах, для тестирования
Тут восстанавливаются записи в списках text files/
Этот модуль не попадёт в релизную версию
'''

from work_file import create_dict_from_list, write_in_file

with open('restore_data/completed(sort).txt', 'r', encoding='UTF-8') as file:
    text_completed = file.readlines()
    text_completed = create_dict_from_list(text_completed)
with open('restore_data/planned(sort).txt', 'r', encoding='UTF-8') as file:
    text_planned = file.readlines()
    text_planned = create_dict_from_list(text_planned)
with open('restore_data/stubs.txt', 'r', encoding='UTF-8') as file:
    text_stubs = file.readlines()
    text_stubs = create_dict_from_list(text_stubs)

with open('text files/planned.txt', 'w', encoding='UTF-8') as file:
    write_in_file(text_planned, file)
with open('text files/completed.txt', 'w', encoding='UTF-8') as file:
    write_in_file(text_completed, file)
with open('text files/liked.txt', 'w', encoding='UTF-8') as file:
    write_in_file(text_stubs, file)
with open('text files/dropped.txt', 'w', encoding='UTF-8') as file:
    write_in_file(text_stubs, file)
