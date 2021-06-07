import json

my_dict = dict()
aver_income = 0
n = 0

with open("text_7.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, type, proceeds, cost = line.split()
        income = int(proceeds) - int(cost)
        if income >= 0:
            aver_income += income
            n += 1
        my_dict[name] = income
aver_income /= n
with open("task_7.json", "w", encoding="utf-8") as f:
    json.dump([my_dict, {"Средний доход: ": aver_income}], f, ensure_ascii=False)