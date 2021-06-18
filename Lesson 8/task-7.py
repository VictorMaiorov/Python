class ComplexNumber:
    def __init__(self, n_1, n_2):
        self.number = complex(n_1, n_2)
        print(f'Преобразование в комплексное число: {self.number}')

    def __add__(self, other):
        return f'Сумма: {self.number + other.number}'

    def __mul__(self, other):
        return f'Произведение: {self.number * other.number}'


num_1 = ComplexNumber(2, 5)
num_2 = ComplexNumber(6, 3)
print(num_1 + num_2)
print(num_1 * num_2)
