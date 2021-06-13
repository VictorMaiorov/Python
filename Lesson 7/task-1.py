class Matrix:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        line = []
        matrix = []
        for string in self.num:
            for el in string:
                line.append(str(el))
            matrix_str = '\t'.join(line)
            matrix.append(matrix_str)
            line = []
        return '\n'.join(matrix)

    def __add__(self, other):
        matrix_sum = []
        str_sum = []
        n = 0
        for str_item in self.num:
            for i, el in enumerate(str_item):
                str_sum.append(self.num[n][i] + other.num[n][i])
            matrix_sum.append(str_sum)
            str_sum = []
            n += 1
        return Matrix(matrix_sum)


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
mat_1 = Matrix(matrix_1)
mat_2 = Matrix(matrix_2)
mat_sum = mat_1 + mat_2

print(mat_1)
print()
print(mat_2)
print()
print(mat_sum)
