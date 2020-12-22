list_base = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [n for n in list_base if n > list_base[list_base.index(n) - 1] and list_base.index(n) != 0]

print(new_list)
