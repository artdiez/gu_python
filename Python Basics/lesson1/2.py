# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

input_time = int(input('Введите количество секунд: '))
hours = input_time // 3600
minutes = (input_time - hours * 3600) // 60
seconds = input_time - (hours * 3600 + minutes * 60)

print(f'Время в формате чч:мм:сс: {hours}:{minutes}:{seconds}')