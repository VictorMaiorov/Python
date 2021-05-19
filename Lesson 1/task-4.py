number = int(input("Введите число: "))
max_number = number % 10
number = number // 10
while number != 0:
    if max_number < number % 10:
        max_number = number % 10
    number = number // 10
print(f"Самая большая цифра в числе: {max_number}")