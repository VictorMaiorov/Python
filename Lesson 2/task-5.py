my_list = [7, 5, 3, 3, 2]
i = 0
k = 0
while True:
    my_list.reverse()
    n = int(input("Введите число: "))
    while i < len(my_list):
        if n == my_list[i]:
            my_list.insert(i + my_list.count(n), n)
            i = 0
            break
        else:
            i += 1
        if n > my_list[i - 1]:
            k = i
    else:
        my_list.insert(k, n)
        i = 0
        k = 0
    my_list.reverse()
    print(my_list)