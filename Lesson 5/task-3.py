with open("task_3.txt", "r", encoding="utf-8") as f:
    content = f.read().splitlines()
    min_salary = 20000
    average_salary = 0
    n = 0
    m = 1
    print("Сотрудники, оклад которых ниже 20 тыс.:")
    for el in content:
        salary = float(el[-7:])
        if salary >= min_salary:
            print(f"{m}. {el}")
            m += 1
        average_salary += float(el[-7:])
        n += 1
print(f"Средняя зарплата всех {n} сотрудников: {(average_salary / n):.1f}")
