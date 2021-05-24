my_list = list(input("Заполните список: "))
i = 0
if len(my_list) % 2 == 0:
    n = len(my_list)
else: n = len(my_list)-1
while i < n:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(my_list)