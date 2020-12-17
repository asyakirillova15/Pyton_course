def check_email():
    while True:
        address = input("Введите ваш email: ")
        if address.count("@") and len(address) > 2:
            return address
        print("Неверный формат email")


def check_year():
    while True:
        try:
            year_born = int(input("Введите год вашего рождения: "))
            if 1900 < year_born < 2020:
                return year_born
        except ValueError:
            pass
        print("Введите корректный год рождения")


def check_empty(hint):
    while True:
        value = input(hint)
        if not value:
            print("Введите данные")
        else:
            return value


def my_func(val_name, val_surname, val_year, val_sity, val_email, val_tel):
    return f"Пользователь {val_name} {val_surname}, " \
           f"{val_year} года рождения, из города {val_sity}, " \
           f"контактные данные: {val_email}  {val_tel}"


email = check_email()
name = check_empty("Введите ваше имя: ").title()
tel = check_empty("Введите ваш номер телефона: ")
surname = check_empty("Введите вашу фамилию: ").title()
sity = check_empty("Введите ваш город: ").title()
year = check_year()

print(my_func(val_email=email, val_name=name, val_tel=tel, val_surname=surname, val_sity=sity, val_year=year))
