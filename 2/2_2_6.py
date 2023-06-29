class WindowDlg:
    def __init__(self, title: str, width: int, height: int):
        if type(title) == str and type(width) == type(height) == int:
            self.__title = title
            self.__width = width
            self.__height = height
        else:
            raise ValueError("Введите корректные данные")

    def show(self):
        print(f'{self.title}: {self.width}, {self.__height}')

    @classmethod
    def __check_int(cls, value):
        return True if type(value) == int and 0 <= value <= 10000 else False

    @property
    def title(self):
        return self.__title

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__check_int(width):
            temp = self.__width
            self.__width = width
            if temp != self.__width:
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check_int(height):
            temp = self.__height
            self.__height = height
            if temp != self.__height:
                self.show()
