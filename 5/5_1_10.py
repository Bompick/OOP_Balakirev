class Triangle:
    def __init__(self, *args):
        if len(args) !=3:
            raise ArithmeticError("У треугольника должно быть 3 стороны")

        a, b, c = list(map(self.check_type, args))

        if self.check_triangle(a, b, c):
            self._a = a
            self._b = b
            self._c = c

    @staticmethod
    def check_type(value):
        if type(value) in (int, float) and value > 0:
            return value
        else:
            raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def check_triangle(a, b, c):
        if a < b+c and b < a+c and c < a+b:
            return True
        else:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3),
              (-3, 3, 5.2), (4.2, 5.7, 8.7),
              (True, 3, 5), (7, 4, 6)]

lst_tr = list()
for item in input_data:
    try:
        a = Triangle(*item)
        lst_tr.append(a)
    except (ValueError, TypeError, ArithmeticError):
        pass




