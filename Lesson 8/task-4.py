class EquipmentWarehouse:
    warehouse = []

    def __init__(self, warehouse_size):
        print('Склад создан')
        self.warehouse_size = warehouse_size  # Размер склада


class Equipment:
    def __init__(self, firm, model, cost):
        self.model = model  # Название модели
        self.firm = firm  # Название фирмы
        self.cost = cost  # Цена товара
        print(f'Товар {self.__class__.__name__} добавлен')


class Printer(Equipment):
    def __init__(self, firm, model, cost, print_speed):
        super().__init__(firm, model, cost)
        self.print_speed = print_speed  # Скорость печати
        self.unit = {'Тип': self.__class__.__name__, 'Фирма': self.firm, 'Модель': self.model, 'Цена': self.cost}
        EquipmentWarehouse.warehouse.append(self.unit)


class Scanner(Equipment):
    def __init__(self, firm, model, cost, color_bit_depth):
        super().__init__(firm, model, cost)
        self.color_bit_depth = color_bit_depth  # Колличество цветов
        self.unit = {'Тип': self.__class__.__name__, 'Фирма': self.firm, 'Модель': self.model, 'Цена': self.cost}
        EquipmentWarehouse.warehouse.append(self.unit)


class CopyMachine(Equipment):
    def __init__(self, firm, model, cost, scanning_speed):
        super().__init__(firm, model, cost)
        self.scanning_speed = scanning_speed  # Скорость сканирования
        self.unit = {'Тип': self.__class__.__name__, 'Фирма': self.firm, 'Модель': self.model, 'Цена': self.cost}
        EquipmentWarehouse.warehouse.append(self.unit)


eq_wa = EquipmentWarehouse(10)
eq = Equipment
print('Начинаем пополнять склад')
n_1 = Printer('KYOCERA', 'Ecosys P2335dn', 15500, 35)
n_2 = Printer('KYOCERA', 'Ecosys P4564dn', 12500, 30)
n_3 = Scanner('CANON', 'Canoscan LIDE300', 5780, 48)
n_4 = Scanner('CANON', 'Canoscan LIDE7000', 9770, 100)
n_5 = CopyMachine('KYOCERA', 'Ecosys M2835dw', 37000, 40)
n_6 = CopyMachine('KYOCERA', 'Ecosys M5678dw', 50000, 90)
print('Закончили пополнять склад')
print('Товары на складе:')
for el in eq_wa.warehouse:
    print(el)
