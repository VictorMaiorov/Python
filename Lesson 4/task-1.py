from sys import argv

my_list = [int(i) for i in argv[1:]]
print(f"Зарплата сотрудника за этот месяц составит {(my_list[0] * my_list[1]) + my_list[2]}₽")
