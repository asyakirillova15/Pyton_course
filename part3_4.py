def check_input(hint):
    while True:
        value = input(hint)
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                print("Нет, нужно ввести число")


def check_input_2(hint):
    while True:
        value = input(hint)
        try:
            return int(value)
        except ValueError:
            try:
                return int(value)
            except ValueError:
                print("Нет, нужно ввести число")


num_1 = check_input("Данная функция выполняет возведение в отрицательную степень\nВведите первое число: ")
num_2 = abs(check_input_2("Введите второе число (целое, отрицание мы добавим сами): "))


def my_func(x, y):
    var = 1 / (x**y)
    return var


result = my_func(num_1, num_2)
print(f"Результат возведения числа {num_1} в {-num_2} степень:"
      f"{result: 5)}")
