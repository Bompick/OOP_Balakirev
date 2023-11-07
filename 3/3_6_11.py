import math
class Integer:
    def __set_name__(self, owner, name):
        self.name ="_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        if self.check(a, b, c):
            self.a = a
            self.b = b
            self.c = c

    @classmethod
    def check(cls, *args):
        if len(args) != 3:
            raise ValueError("это не треугольник")
        for i in args:
            if type(i) not in (float, int) or i <= 0:
                raise ValueError("длины сторон треугольника должны быть положительными числами")
        a, b, c = args
        if a < b+c and b < a+c and c < a+b:
            return True
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = self.__len__()/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


tr = Triangle(3, 4, 5)
assert tr.a == 3 and tr.b == 4 and tr.c == 5, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"