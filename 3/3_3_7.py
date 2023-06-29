from math import sqrt
class Complex:

    def __init__(self, real, img):
        if self.to_check(real) and self.to_check(img):
            self.__real = real
            self.__img = img

    @classmethod
    def to_check(cls, x):
        if type(x) in (int, float):
            return True
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if self.to_check(real):
            self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if self.to_check(img):
            self.__img = img

    def __abs__(self):
        return sqrt(self.real*self.real + self.img*self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
