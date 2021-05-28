def my_f(n1, n2, n3):
    s = [n1, n2, n3]
    s.remove(min(s))
    return sum(s)


num1, num2, num3 = input("Введите три числа через пробел: ").split(" ")
print(my_f(int(num1), int(num2), int(num3)))
