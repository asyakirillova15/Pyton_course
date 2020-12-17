def parse_input(hint):
    while True:
        value = input(hint)
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                print("Нет, нужно ввести число")


num_1 = parse_input("Введите первое число: ")
num_2 = parse_input("Введите второе число: ")
num_3 = parse_input("Введите третье число: ")

def my_func(arg_1, arg_2, arg_3):
    my_list_1 = [arg_1, arg_2, arg_3]
    max_1 = max(my_list_1)
    my_list_1.remove(max_1)
    max_2 = max(my_list_1)
    return max_1 + max_2

print(my_func(num_1, num_2, num_3))
