proceeds = int(input("Какая выручка у фирмы за месяц? "))
costs = int(input("Какаие издержки? "))
result = proceeds - costs
if result > 0:
    print("Фирма в этот месяц отработала с прибылью.")
    print(f"Рентабельность выручки при этом составила {result / proceeds}")
    number_of_employees = int(input("Какое количество сотрудников в вашей фирме? "))
    profit = int(result / number_of_employees)
    print(f"Прибыль фирмы в расчете на одного сотрудника составила {profit} р.")
else: print("Фирма в этот месяц отработала с убытком.")