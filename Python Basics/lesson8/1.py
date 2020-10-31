# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def exicute(cls, data):
        day,month,year = str(data).split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validate(data):
        day, month, year = str(data).split('-')
        if int(day) in range(1, 32) and int(month) in range(1, 13) and int(year) in range(1900, 2990):
            return True
        else:
            return False

data = Data(1-12-1990)
print(Data.exicute('1-12-1990'))
print(Data.validate('1-11-1790'))
