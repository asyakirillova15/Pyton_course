def check_value(value):
    if not value.isdigit():
        return False
    else:
        return int(value)


def fact(num):
    factorial_ = 1
    for i in range(1, num + 1, 1):
        factorial_ = factorial_ * i
        yield factorial_


n = False
while not n:
    n = input("Введите только целое положительное число: ")
    n = check_value(n)


my_generator = fact(n)
for el in my_generator:
    print(el)
