lesson_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(lesson_list)
my_list = [el for el in lesson_list if lesson_list.count(el) == 1]
print(my_list)
