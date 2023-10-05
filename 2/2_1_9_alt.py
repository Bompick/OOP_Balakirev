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
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.get_coords()[0].get_coords()} {self.get_coords()[-1].get_coords()}')

r1 =Point(1,2)

rect= Rectangle(0, 0, 20, 34)

assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), "атрибуты __sp и __ep должны ссылаться на объекты класса Point"