class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input("Введите целое число 1: ")
num_2 = input("Введите целое число 2: ")
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise OwnError("Делитель не должен быть равен 0")
except (ValueError, OwnError) as err:
    print(err)
else:
    print(num_1 / num_2)
