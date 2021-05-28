def my_f(x, y):
    print(f"{x ** y}")
    i = 0
    n = 1
    y = abs(y)
    while i < y:
        n = n * x
        i += 1
    print(1 / n)


while True:
    try:
        n1, n2 = input("Введите через пробел два числа, действительное положительное и целое отрицательное: ").split(
            " ")
        n1 = float(n1)
        n2 = int(n2)
    except ValueError:
        print("Не верный ввод")
    else:
        if n2 > 0:
            print("Второе число не отрицательное")
        elif n1 < 0:
            print("Первое число не положительное")
        else:
            my_f(n1, n2)
