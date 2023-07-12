class ItemAttrs:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


class Point(ItemAttrs):
    pass


pt = Point(1, 2.5)
x = pt[0]
y = pt[1]
print(x, y, sep='\n')
pt[0] = 10
print(pt.coords)
