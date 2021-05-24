my_list = input("Введите слова через пробел: ")
i = 0
n = 1
while i <= (len(my_list.split())-1):
    print(f"{n:2d}. {(my_list.split()[i][:10])}")
    i += 1
    n += 1