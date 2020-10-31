# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('4_src.txt') as f:
    content = f.read().split('\n')

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('4.txt', 'w+') as f:
    for string in content:
        string = string.split(' ', 1)
        f.write(translate.get(string[0]) + ' ' + string[1] + '\n')
