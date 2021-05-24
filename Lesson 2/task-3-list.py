user_month = int(input("Введите номер месяца: "))
if user_month > 12 or user_month < 1:
    print("В году 12 месяцев")
else:
    list_month = ["Зима", "Весна", "Лето", "Осень"]
    if user_month == 12 or user_month == 1 or user_month == 2:
        print(list_month[0])
    elif user_month == 3 or user_month == 4 or user_month == 5:
        print(list_month[1])
    elif user_month == 6 or user_month == 7 or user_month == 8:
        print(list_month[2])
    else:
        print(list_month[3])