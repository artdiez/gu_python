# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

input_number = input('Введите целое положительно число: ')
index = 0
max = 0
while index < len(input_number):
    if int(input_number[index]) > max:
        max = int(input_number[index])
    index += 1
print('Max number: ' + str(max))