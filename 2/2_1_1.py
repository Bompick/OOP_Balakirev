class Point:
    def __init__(self, x =0 , y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coords(self, x,  y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coords(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coords(15, 30)
print(pt.get_coords())

print(dir(pt))
print(pt._Point__x)
