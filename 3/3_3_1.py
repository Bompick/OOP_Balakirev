class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return  f'{self.name} -REPR'

    def __str__(self):
        return f"{self.name} ---str "


cat = Cat("Жпулька")
print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return tuple(map(abs, self.__coords))


p = Point(1, 2, -5, 4, -99)
print(len(p))
print(abs(p))
