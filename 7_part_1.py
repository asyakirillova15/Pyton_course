class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        new_matrix = []
        counter_list = 0

        for el in self.matrix:
            new_mini = []
            counter_index = 0
            for value_1 in el:
                value_2 = other.matrix[counter_list][counter_index]

                sum_el = value_1 + value_2
                counter_index += 1
                new_mini.append(sum_el)

            counter_list += 1
            new_matrix.append(new_mini)
        return Matrix(new_matrix)


matrix_1 = Matrix([[1, 2, 8], [2, 3, 7], [45, 8, 8]])
matrix_2 = Matrix([[12, 12, 9], [3, 7, 9], [5, 5, 1]])
matrix_3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_2 + matrix_3 + matrix_3)
