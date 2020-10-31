# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroException:
    def __init__(self,divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def division(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return 'Делить на ноль нельзя!'

print(ZeroException.division(2,0))
print(ZeroException.division(2,2))