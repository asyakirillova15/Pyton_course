class Cell:
    def __init__(self, alveola):
        self.alveola = alveola

    def __add__(self, other):
        return Cell(self.alveola + other.alveola)

    def __sub__(self, other):
        if self.alveola > other.alveola:
            return Cell(self.alveola - other.alveola)
        else:
            return f"Вычитание выполнить невозможно, т.к. результат должен быть положительным!"

    def __mul__(self, other):
        return Cell(self.alveola * other.alveola)

    def __floordiv__(self, other):
        if self.alveola == 0 or other.alveola == 0:
            return "Поделить не получится"
        else:
            if self.alveola >= other.alveola:
                return Cell(round(self.alveola / other.alveola))
            else:
                return Cell(round(other.alveola / self.alveola))

    def __str__(self):
        return f"Клетка с ячейками {self.alveola}"

    def make_order(self, num_character):
        cell = ""
        counter = 0
        while counter < self.alveola:
            counter += 1
            cell += "*"
        number_of_line = len(cell) // num_character
        result = ""
        ind = 0
        count = 0
        while count < number_of_line:
            result += cell[ind:ind + num_character] + "\n"
            ind += num_character
            count += 1
        if len(cell) % num_character != 0:
            index_residue = len(cell) - num_character * number_of_line
            result += cell[-index_residue:]

        return result


cell_1 = Cell(12)
cell_2 = Cell(19)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(8))
