# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

summa = 0

while True:
    numbers = input('Введите строку чисел, разделенных пробелом (Для выхода нажимете клавишу Q): ').split()
    if 'Q' in numbers:
        if numbers.index('Q') == 0:
            print('Завершение работы')
            break
        else:
            for i in numbers[:numbers.index('Q')]:
                summa += int(i)
            print(summa)
            print('Завершение работы')
            break
    else:
        for i in numbers:
            summa += int(i)
        print(summa)
