def format_input(hint):
    while True:
        input_value = input(hint)
        try:
            return int(input_value)
        except ValueError:
            try:
                return float(input_value)
            except ValueError:
                print("Нет, нужно ввести число")


val_1 = format_input("Введите число 1: ")
val_2 = format_input("Введите число 2: ")


def my_division(arg_1, arg_2):
    try:
        return round(arg_1 / arg_2, 2)
    except ZeroDivisionError:
        return "Делить на ноль запрещено"


print(my_division(val_1, val_2))
