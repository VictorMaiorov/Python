my_dict = dict()
with open("text_6.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, value = line.split(':')
        value = value.split()
        sum_num = 0
        for el in value:
            if el == "-":
                continue
            num, type_subj = el.split("(")
            sum_num += int(num)
        my_dict[name] = sum_num
print(my_dict)
