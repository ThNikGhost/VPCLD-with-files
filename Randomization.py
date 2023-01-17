# Рандомит список из "Буду смотреть(по порядку).txt" в "Буду смотреть(рандом).txt"
from random import shuffle
from Main import Create_dict, Write
later_po = open('text files/planned.txt', 'r', encoding='UTF-8')
later_ran = open('text files/planned(random).txt', 'w', encoding='UTF-8')

text_sorted = later_po.readlines()  # получает данные из файла "Буду смотреть(по порядку).txt"
shuffle(text_sorted) # разбрасывает элементы
text_ran = Create_dict(len(text_sorted), text_sorted) # см "переменные.py"
Write(text_ran, later_ran) # см "переменные.py"

later_ran.close()
later_po.close()