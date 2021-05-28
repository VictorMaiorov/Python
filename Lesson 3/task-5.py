def my_f():
    numbers = []
    sum_num = 0
    while True:
        try:
            break_flag = False
            num_user = input("Введите числа через пробел для суммирования или Q для завершения \n").split()
            for el in num_user:
                if el == 'Q':
                    break_flag = True
                else:
                    numbers.append(int(el))
            print(sum_num + sum(numbers))
            if break_flag:
                break
        except ValueError:
            print("Так не пойдёт, надо вводить или числа или Q")
    return


my_f()
