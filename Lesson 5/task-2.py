with open("task_2.txt", "r", encoding="utf-8") as f:
    content = f.read().splitlines()
    n = len(content)
    i = 0
    print(f"В файле {n} строк")
    while i < n:
        m = len(content[i].split())
        print(f"В {i + 1} строке слов: {m}")
        i += 1
