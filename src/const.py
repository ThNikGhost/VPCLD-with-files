'''Технический модуль, для теста, чтобы быстро восстанавливать данные в файлах, для тестирования
Тут восстанавливаются записи в списках
Этот модуль не попадёт в релизную версию(если она будет)
'''
from work_file import creating_dict, writing

with open('file_const/completed(sort).txt', 'r', encoding='UTF-8') as file:
    text_completed = file.readlines()
    text_completed = creating_dict(text_completed)
with open('file_const/planned(sort).txt', 'r', encoding='UTF-8') as file:
    text_planned = file.readlines()
    text_planned = creating_dict(text_planned)
with open('file_const/stubs.txt', 'r', encoding='UTF-8') as file:
    text_stubs = file.readlines()
    text_stubs = creating_dict(text_stubs)

with open('text files/planned.txt', 'w', encoding='UTF-8') as file:
    writing(text_planned, file)
with open('text files/completed.txt', 'w', encoding='UTF-8') as file:
    writing(text_completed, file)
with open('text files/liked.txt', 'w', encoding='UTF-8') as file:
    writing(text_stubs, file)
with open('text files/dropped.txt', 'w', encoding='UTF-8') as file:
    writing(text_stubs, file)
