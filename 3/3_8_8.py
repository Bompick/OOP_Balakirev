class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return tuple(self.coords[item.start:item.stop:item.step])
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1])
v[:] = 1, 2, 3, 4
print(v[2])
print(v[1:])
v[0] = 10.5

