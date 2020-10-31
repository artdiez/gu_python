# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

list_rating = [7, 5, 3, 3, 2]

rating = int(input('Введите новый элемент рейтинга: '))

for index in range(len(list_rating)):
    if list_rating[index] == rating:
        list_rating.insert(index + 1, rating)
        break
    elif list_rating[0] < rating:
        list_rating.insert(0, rating)
        break
    elif list_rating[-1] > rating:
        list_rating.append(rating)
        break
    elif list_rating[index] > rating and list_rating[index + 1] < rating:
        list_rating.insert(index + 1, rating)
        break

print(list_rating)