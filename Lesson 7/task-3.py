class Cell:
    def __init__(self, cells_number):
        self.cells_number = cells_number

    def make_order(self, n):
        result = ['*' * n * (self.cells_number // n)]
        if self.cells_number % n:
            result.append('*' * (self.cells_number % n))
        return '\n'.join(result)

    def __str__(self):
        return f"{self.cells_number}"

    def __add__(self, other):  # сложение
        return f"Сумма: {Cell(self.cells_number + other.cells_number)}"

    def __sub__(self, other):  # вычитание
        if self.cells_number < other.cells_number:
            raise ValueError("Разность меньше нуля")
        return f"Разность: {Cell(self.cells_number - other.cells_number)}"

    def __mul__(self, other):  # умножение
        return f"Произведение: {Cell(self.cells_number * other.cells_number)}"

    def __floordiv__(self, other):  # деление
        return f"Частность: {Cell(self.cells_number // other.cells_number)}"


cell_1 = Cell(20)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(25))
# print(cell_2.make_order(7))
# print(cell_2.make_order(11))
# print(cell_2.make_order(2))
