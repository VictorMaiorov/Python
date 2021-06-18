class Date:
    def __init__(self, input_date):
        self.input_date = str(input_date)

    @classmethod
    def date(cls, input_date):
        user_date = []
        for el in input_date.split('.'):
            user_date.append(el)
        return int(user_date[0]), int(user_date[1]), int(user_date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year <= 2021:
                    return 'Проверка даты: всё в порядке, валидация пройдена.'
                else:
                    return 'Проверка даты: год больше, чем 2021, валидация не пройдена.'
            else:
                return 'Проверка даты: такой месяц не существует, валидация не пройдена.'
        else:
            return 'Проверка даты: такого числа нет в календаре, валидация не пройдена.'

    def __str__(self):
        return f'Введенная дата: {Date.date(self.input_date)}'


date_1 = Date('16.6.2021')
print(date_1)
print(Date.validation(16, 6, 2021))
print(Date.validation(6, 16, 2021))
print(Date.validation(59, 16, 2021))
print(Date.validation(6, 6, 2029))
print(Date.date('16.6.2021'))
