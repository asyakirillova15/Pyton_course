class Complex_number:
    def __init__(self, complex_):
        self.list = complex_.split(' ')
        self.a = int(self.list[0])
        if self.list[1] == '+':
            self.b = int(self.list[2][:-1])
        else:
            self.b = -int(self.list[2][:-1])

    def __add__(self, other):
        num_1, num_2, symbol = self.transform_other(other)
        sum_2 = self.b + num_2
        if sum_2 < 0:
            symbol = "-"
            sum_2 = sum_2 * (-1)
        elif sum_2 == 0:
            return self.a + num_1
        return f"{(self.a + num_1)} {symbol} {sum_2}j"

    def __mul__(self, other):
        num_1, num_2, symbol = self.transform_other(other)
        sum_2 = self.b * num_1 + self.a * num_2
        if sum_2 < 0:
            symbol = "-"
            sum_2 = sum_2 * (-1)
        elif sum_2 == 0:
            return self.a * num_1 - self.b * num_2
        return f"{(self.a * num_1 - self.b * num_2)} {symbol} {sum_2}j"

    @staticmethod
    def transform_other(other):
        other = other.split(' ')
        num_1 = int(other[0])
        if other[1] == '+':
            num_2 = int(other[2][:-1])
        else:
            num_2 = -int(other[2][:-1])
        symbol = "+"
        return num_1, num_2, symbol


one = Complex_number("-3 - 1j")
print(one.__add__("51 + 15j"))
print(one.__mul__("-8 - 5j"))
