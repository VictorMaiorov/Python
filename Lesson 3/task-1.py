def my_f(a_1, a_2):
    sub = a_1 / a_2
    return print(sub)


arg_1 = int(input("Что делим? "))
arg_2 = int(input("На что делим? "))
if arg_2 == 0:
    print("Не хочу делить на 0")
else:
    my_f(arg_1, arg_2)
