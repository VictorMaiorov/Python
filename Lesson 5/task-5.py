from random import randrange

my_list = []
list_length = int(input("Длина списка: "))
while len(my_list) < list_length:
    my_list.append(str(randrange(100)))
print(f"Генерируем список из {list_length} элементов:\n{' '.join(my_list)}")
print("Записываем данные в файл...")
with open("task_5.txt", "w", encoding="utf-8") as f_1:
    print(' '.join(my_list), file=f_1)
print("Читаем данные из файла...")
sum_num = 0
with open("task_5.txt", "r", encoding="utf-8") as f_2:
    content = f_2.read().split()
    for el in content:
        sum_num += int(el)
print(f"Сумма чисел: {sum_num}")
