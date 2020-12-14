my_str = input("Введите текст: ")
for ind, el in enumerate(my_str.title().split()):
    print(ind + 1, el[:10])
