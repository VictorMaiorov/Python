def int_func():
    return user_word.title()


user_words = input("Введите слово из строчных латинских букв: ").split()
m = []
for user_word in user_words:
    m.append(int_func())
print(m)
