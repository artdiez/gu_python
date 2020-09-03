# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    max1 = max(args)
    args.remove(max1)
    max2 = max(args)
    return max1 + max2

print(my_func(13, 12.5, 40))