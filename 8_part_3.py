class ErrNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


list_numbers = []
user_value = ''
while user_value != 'stop':
    user_value = input("Для выхода из программы введите 'stop'. Введите число: ")
    try:
        user_value = int(user_value)

        if user_value <= 0:
            raise ErrNumber("Введите положительное число!")
    except ValueError as err:
        try:
            user_value = float(user_value)
            raise ErrNumber("Нужно целое число!")
        except (ValueError, ErrNumber) as err:
            print(err)
    except ErrNumber as err:
        print(err)
    else:
        list_numbers.append(int(user_value))
print(list_numbers)
