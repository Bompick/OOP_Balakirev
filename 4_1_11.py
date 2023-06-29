class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def check_len(self, obj):
        if len(self) != len(obj):
            raise TypeError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if self.check_len(other):
            prom_coords = tuple([j+other.coords[i] for i, j in enumerate(self.coords)])
            if all(map(lambda x: type(x) is int, prom_coords)):
                return VectorInt(*prom_coords)
            else:
                return Vector(*prom_coords)

    def __sub__(self, other):
        if self.check_len(other):
            return Vector(*tuple([j-other.coords[i] for i, j in enumerate(self.coords)]))

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *args):
        if all(map(lambda x: type(x) is int, args)):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')


v1 = Vector(1, 2.3, 3)


v2 = VectorInt(1, 2, 3)
v3 = VectorInt(4, 5, 6)
vu = v1 + v2
va = v2 + v3

