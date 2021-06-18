class DivisionByNull(Exception):
    pass


while True:
    try:
        n_1 = float(input('Что делим? '))
        n_2 = float(input('На что делим? '))
        if n_2 == 0:
            raise DivisionByNull('Деление на ноль!')
    except DivisionByNull as err:
        print(err)
    except ValueError:
        print('Не верный ввод.')
    else:
        print(f'Результат деления: {(n_1 / n_2):.03f}.')
