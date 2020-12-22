from sys import argv

name, hours_user, rate_user, bonus_user = argv


def my_pay(hours_a, rate_a, bonus_a):
    pay = hours_a * rate_a + bonus_a
    return round(pay, 3)


def check_value(value):
    try:
        if int(value) > 0:
            return int(value)
        else:
            raise TypeError("Число должно быть положительным")
    except ValueError:
        if float(value) > 0:
            return float(value)
        else:
            raise TypeError("Число должно быть положительным")


try:
    hours = check_value(hours_user)
    rate = check_value(rate_user)
    bonus = check_value(bonus_user)
    print(f"Заработная плата сотрудника равна: {my_pay(hours, rate, bonus)}у.е.")
except ValueError:
    print("Необходимо ввести число")
except TypeError as err:
    print(err)
