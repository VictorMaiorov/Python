my_dict = {0: "Ноль", 1: "Один", 2: "Два", 3: "Три", 4: "Четыре", 5: "Пять",
           6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять"}

my_list = []

with open("text_4.txt", "r", encoding="utf-8") as file_1:
    content = file_1.read().splitlines()
    for el in content:
        number = int(el[-1])
        string = f"{my_dict.get(number)} - {int(el[-1])}"
        my_list.append(string)

with open("task_4.txt", "w", encoding="utf-8") as file_2:
    for el in my_list:
        print(f"{el}", file=file_2)
print("Перевод завершён")
