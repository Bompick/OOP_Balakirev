from math import sqrt
class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) is int:
            self.coords = [0 for i in range(args[0])]

        elif len(args) > 1 and all(map(lambda x: type(x) in (int, float), args)):
            self.coords = list(args)

    def get_coords(self):
        return self.coords

    def set_coords(self, *args):
        if len(args) == len(self.coords):
            self.coords = list(args)
        elif len(args) > len(self.coords):
            self.coords = list(args[:len(self.coords)])
        elif len(args) < len(self.coords):
            for i in range(len(args)):
                self.coords[i] = args[i]

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sqrt(sum([i**2 for i in self.coords]))


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
vector3D.set_coords(9, 8, 7, 10, 11)
vector3D.set_coords(1, 2)
print(len(vector3D))
print(abs(vector3D))