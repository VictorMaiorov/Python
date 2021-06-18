class MyOwlError(Exception):
    pass


my_list = []
print('Введите stop для остановки ввода')
while True:
    user_input = input("Введите число: ")
    try:
        if user_input == 'stop':
            break
        if user_input == int(user_input):
            raise MyOwlError('Введено не число!')
            # я не понял, как сделать через raise, программа в любом случае уходит в ValueError
    except MyOwlError as err:
        print(err)
    except ValueError:
        print('Введено не число! ValueError')
        continue
    my_list.append(user_input)
print(my_list)
