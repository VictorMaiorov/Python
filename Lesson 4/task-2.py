from random import randrange

my_list = []
list_length = int(input("Длина списка: "))
while len(my_list) < list_length:
    my_list.append(randrange(100))
print(f"Список из случайных элементов:\n{my_list}")

new_list_2 = [el for i, el in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(f"Элементы исходного списка, значения которых больше предыдущего элемента:\n{new_list_2}")
