# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divizion(var1, var2):
    try:
        return var1/var2
    except ZeroDivisionError:
        return 'Деление на ноль!'

print(divizion(int(input('Введите первое число: ')),int(input('Введите второе число: '))))