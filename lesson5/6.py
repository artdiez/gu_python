# 6.Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lessons = {}

with open('6.txt') as f:
    for string in f:
        subject, lecture, practice, lab = string.split()
        lecture = int(lecture.replace('(л)', '')) if lecture != '—' else 0
        practice = int(practice.replace('(пр)', '')) if practice != '—' else 0
        lab = int(lab.replace('(лаб)', '')) if lab != '—' else 0
        lessons[subject] = int(lecture) + int(practice) + int(lab)

print(lessons)