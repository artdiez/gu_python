# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    mounth = int(input('Введите номер месяца от 1 до 12: '))
    if mounth in range(1,13):
        break
    else:
        print('Указано неверное значение! Повторите ввод!')

# With dict

dict_seasons = {'winter': (12, 1, 2), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11)}

for key in dict_seasons.keys():
    if mounth in dict_seasons[key]:
        print(key)

# With list

list_seasons = [['winter', 12, 1, 2],['spring', 3, 4, 5], ['summer', 6, 7, 8], ['autumn', 9, 10, 11]]
for list in list_seasons:
    if mounth in list:
        print(list[0])