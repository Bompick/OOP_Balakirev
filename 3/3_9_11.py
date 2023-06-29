class Matrix:
    def __init__(self, *args):
        if len(args) != 1 and self.check_type_1(args):
            self.rows = args[0]
            self.cols = args[1]
            self.fill = args[2]
            self.matrix = [list([self.fill]*self.cols) for i in range(self.rows)]
        elif len(args) == 1 and self.check_type_2(args):
            self.matrix = args[0]
            self.rows = len(self.matrix)
            self.cols = len(self.matrix[0])

    def __getitem__(self, item):
        row, col = item
        return self.matrix[row][col]

    def __setitem__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        else:
            row, col = key
            self.matrix[row][col] = value

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return Matrix([[x+other for x in row]for row in self.matrix])
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')
        fin = []
        for i, val in enumerate(self.matrix):
            prom = []
            for x, y in enumerate(val):
                prom.append(y+other.matrix[i][x])
            fin.append(prom)
        return Matrix(fin)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            return Matrix([[x-other for x in row]for row in self.matrix])
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')
        fin = []
        for i, val in enumerate(self.matrix):
            prom = []
            for x, y in enumerate(val):
                prom.append(y-other.matrix[i][x])
            fin.append(prom)
        return Matrix(fin)

    @staticmethod
    def check_type_1(data):
        rows, cols, fill = data
        if type(rows) is not int or type(cols) is not int or type(fill) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        else:
            return True

    @staticmethod
    def check_type_2(data):
        data = data[0]
        t_data = [x for row in data for x in row]
        if all(map(lambda x: len(x) == len(data[0]), data)) and \
                all(map(lambda x: type(x) in (int, float), t_data)):
            return True
        else:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')


m1 = Matrix(4, 5, 3)
m2 = Matrix([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
matrix = m1+m2
print(matrix.matrix)
matrix2 = matrix-m2
print(matrix2.matrix)

