class Vector:
    def __init__(self, *args):
        self.coords = [*args]

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if self.compare(self, other):
            return Vector(*[self.coords[i]+other.coords[i] for i in range(len(self))])

    def __iadd__(self, other):
        if type(other) in (int, float):
            res = []
            for i in self.coords:
                i += other
                res.append(i)
            self.coords = res
            return self
        if self.compare(self, other):
            res = [self.coords[i]+other.coords[i] for i in range(len(self))]
            self.coords = res
        return self


    def __isub__(self, other):
        if type(other) in (int, float):
            res = []
            for i in self.coords:
                i -= other
                res.append(i)
            self.coords = res
            return self
        if self.compare(self, other):
            res = [self.coords[i]-other.coords[i] for i in range(len(self))]
            self.coords = res
        return self

    def __sub__(self, other):
        if self.compare(self, other):
            return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self))])

    def __mul__(self, other):
        if self.compare(self, other):
            return Vector(*[self.coords[i] * other.coords[i] for i in range(len(self))])

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.coords[i] == other.coords[i]:
                pass
            else:
                return False
        return True


    @staticmethod
    def compare(v1, v2):
        if len(v1.coords) == len(v2.coords):
            return True
        else:
            raise ArithmeticError('размерности векторов не совпадают')



v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]
