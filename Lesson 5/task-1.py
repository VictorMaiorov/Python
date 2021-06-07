with open("task_1.txt", "a", encoding="utf-8") as f:
    while True:
        n = input("Text: ")
        if n == "":
            break
        else:
            print(n, file=f)
