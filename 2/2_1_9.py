class Point:
    @classmethod
    def __to_check_int_float(cls, *args):
        if all(map(lambda s: type(s) in(int, float), args)):
            return True
        else:
            raise ValueError('ВВедите целое или вещественное число')

    def __init__(self, *args):
        if self.__to_check_int_float(*args):
            self.__x, self.__y = args

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2 and all(map(lambda s: type(s) is Point, args)):
            self.__sp = args[0]
            self.__ep = args[-1]
        elif len(args) == 4 and all(map(lambda s: type(s) in (int, float), args)):
            self.__sp = Point(*args[:2])
            self.__ep = Point(*args[2:])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp.get_coords(), self.__ep.get_coords()

    def draw(self):
        print(f'Прямоугольник с координатами: {self.get_coords()[0]} {self.get_coords()[-1]}')

r1 =Point(1,2)

