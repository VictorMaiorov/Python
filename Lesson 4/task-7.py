def gen():
    for el in range(2, int(input("До скольки считаем? ")) + 1):
        yield el


my_list = [1]
n = 0
for i in gen():
    my_list.append(i * my_list[n])
    n += 1
print(my_list)
