def sum_elements(num_value):
    global sum_current, general_sum
    sum_current += num_value
    general_sum += num_value


general_sum = 0
flag = True
while flag:
    sum_current = 0
    list_base = (input("Введите числа через пробел: ")).split()
    for el in list_base:
        try:
            sum_elements(int(el))
        except ValueError:
            try:
                sum_elements(float(el))
            except ValueError:
                if el.lower() == "q":
                    print(f"Итог: Текущая сумма:{sum_current}, общая сумма {general_sum}")
                    print("Выход из программы")
                    flag = False
                    break
                else:
                    print("Выход по символу Q")
                    break

    print(f"Текущая сумма:{sum_current}, общая сумма {general_sum}")
