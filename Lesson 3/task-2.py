my_f = lambda a_1, a_2, a_3, a_4, a_5, a_6: print(
    f"Имя: {a_1}, Фамилия: {a_2}, Год рождения: {a_3}, Город: {a_4}, Е-маил: {a_5}, Телефон: {a_6}")

name = input("Имя: ")
surname = input("Фамилия: ")
age = input("Год рождения: ")
city = input("Город: ")
email = input("Е-маил: ")
phone = input("Телефон: ")
my_f(name, surname, age, city, email, phone)
