file_bd_w = open('text files/planned.txt', 'w', encoding='UTF-8')
file_pr_w = open('text files/completed.txt', 'w', encoding='UTF-8')
file_pr_r = open('file_const/completed(sort).txt', 'r', encoding='UTF-8')
file_bd_r = open('file_const/planned(sort).txt', 'r', encoding='UTF-8')
from Main import Create_dict, Write

# Записываю из файла на рабочем столе, в файл в папке "Просмотренные(по порядку)"
text_pr_r = file_pr_r.readlines()
Write(Create_dict(len(text_pr_r), text_pr_r), file_pr_w)
# Записываю из файла на рабочем столе, в файл в папке "Буду смотреть(по порядку)"
text_bd_r = file_bd_r.readlines()
Write(Create_dict(len(text_bd_r), text_bd_r), file_bd_w)

file_bd_r.close()
file_bd_w.close()
file_pr_r.close()
file_pr_w.close()
