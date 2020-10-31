# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('2.txt') as f:
    content = f.readlines()
print(f'Количество строк в файле: {len(content)}')

for index, string in enumerate(content):
    print(f'В строке {index + 1} {len(string.split())} слов')