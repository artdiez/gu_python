# 6.Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Equipment:

    def __init__(self, brand, model, amount):
        self.brand = brand
        self.model = model
        self.amount = amount
        self.storage = []
        self.tmp_storage = []
        self.unit_dict = {'Brand': self.brand, 'Model': self.model, 'Amount': self.amount}

    def reception(self):
        try:
            unit_brand = input('Введите наименование производителя устройства: ')
            unit_model = input('Введите модель устройства: ')
            unit_amount = int(input('Укажите количество: '))
            unit_dict = {'Brand': unit_brand, 'Model': unit_model, 'Amount': unit_amount}
            self.unit_dict.update(unit_dict)
            self.tmp_storage.append(self.unit_dict)
            print(f'Текущий список постановки на приход: \n {self.tmp_storage}')
        except Exception:
            return 'Введены некорректные данные!'
            
        answer = input('Справка: для выхода нажмите клавишу "Q", для продолжения - клавишу "Enter"').lower()
        if answer == 'q':
            self.storage.append(self.tmp_storage)
            print(f'Содержимое склада: \n {self.storage}')
            return 'Выход'
        else:
            return Equipment.reception(self)


class Printer(Equipment):
    def print(self):
        return f'Printer {self.brand} {self.model} is now printing...'

class Scanner(Equipment):
    def scan(self):
        return f'Scanner {self.brand} {self.model} is now scanning...'

class Copier(Equipment):
    def copy(self):
        return f'Copier {self.brand} {self.model} is now copying...'


printer = Printer('HP', 'NP1001', 3)
scanner = Scanner('Canon', 'SC203', 5)
copier = Copier('Xerox', 'XR1200', 1)
print(scanner.scan())
print(printer.reception())