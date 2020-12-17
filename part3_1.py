def format_input(input_value):
    try:
        return int(input_value)
    except ValueError:
        return float(input_value)


def my_division(arg_1, arg_2):
    try:
        return round(arg_1 / arg_2, 2)
    except ZeroDivisionError:
        return "Делить на ноль запрещено"


try:
    val_1 = format_input(input("Введите число 1: "))
    val_2 = format_input(input("Введите число 2: "))
    print(my_division(val_1, val_2))
except ValueError:
    print("Неверный ввод")
