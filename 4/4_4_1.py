class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill



r = Rect(0, 0, 10, 20)
# print(r.__dict__)
print(r.get_coords())
