class Line:
    def __init__(self, *args):
        self.__x1, self.__y1, self.__x2, self.__y2 = args

    def set_coords(self, *args):
        self.__x1, self.__y1, self.__x2, self.__y2 = args

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        for i in self.get_coords():
            print(i, end=' ')
