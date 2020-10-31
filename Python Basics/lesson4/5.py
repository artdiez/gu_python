# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
list = [el for el in range(100, 1001, 2)]

def multiplication (var1, var2):
    return var1*var2

print(reduce(multiplication, list))