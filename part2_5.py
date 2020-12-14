my_list = [7, 6, 3, 2]
while True:
    v1 = int(input("Введите цифру от 1 до 9: "))
    if v1 == 10:
        break
    while v1 <= 0 or v1 > 9:
        v1 = int(input("Будьте внимательнее. Введите цифру еще раз: "))
    for el in my_list:
        if v1 > el:
            my_list.insert(my_list.index(el), v1)
            break
        if my_list.index(el) == len(my_list) - 1:
            my_list.append(v1)
            break
    print(f"{my_list} \n Для выхода нажмите: 10")
