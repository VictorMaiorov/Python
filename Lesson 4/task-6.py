from itertools import count
from itertools import cycle

my_list = []
my_list_2 = []

n = int(input("С какого числа начинаем?\n"))
for el in count(n):
    if el > 20:
        break
    else:
        my_list.append(el)
print(my_list)

с = 1
for el in cycle(my_list):
    if с > 40:
        break
    my_list_2.append(el)
    с += 1
print(my_list_2)
