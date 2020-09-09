# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('3.txt') as f:
    content = f.read().split('\n')

min_salary = []
sum = 0
for el in content:
    el = el.split()
    if int(el[1]) < 20000:
        min_salary.append(el[0])
    sum += int(el[1])

print(f'Сотрудники с окладом менее 20 000: {", ".join(min_salary)}')
print(f'Средняя величина дохода сотрудников: {sum/len(content)}')