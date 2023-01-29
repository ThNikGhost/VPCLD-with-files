# Технический файл, для теста, чтобы быстро восстанавливать данные в файлах, для тестирования
from work_file import CreatingDict, Writing

file_planned = open('text files/planned.txt', 'w', encoding='UTF-8')
file_completed = open('text files/completed.txt', 'w', encoding='UTF-8')
file_liked = open('text files/liked.txt', 'w', encoding='UTF-8')
file_dropped = open('text files/dropped.txt', 'w', encoding='UTF-8')

file_completed_sort = open('file_const/completed(sort).txt', 'r', encoding='UTF-8')
file_planned_sort = open('file_const/planned(sort).txt', 'r', encoding='UTF-8')
file_stubs = open('file_const/stubs.txt', 'r', encoding='UTF-8')

# Записываю из файла completed(sort), в файл в папке "completed.txt"
text_completed = file_completed_sort.readlines()
Writing(CreatingDict(len(text_completed), text_completed), file_completed)
# Записываю из файла planned(sort), в файл в папке "planned.txt"
text_planned = file_planned_sort.readlines()
Writing(CreatingDict(len(text_planned), text_planned), file_planned)
# Записываю из файла stubs, в файлы 'dropped.txt' и 'liked.txt'
text_stubs = file_stubs.readlines()
Writing(CreatingDict(len(text_stubs), text_stubs), file_liked)
Writing(CreatingDict(len(text_stubs), text_stubs), file_dropped)

file_planned_sort.close()
file_planned.close()
file_completed_sort.close()
file_completed.close()
