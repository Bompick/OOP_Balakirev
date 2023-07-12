class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе нужно определить метод 'get_pr' ")


class Rect(Geom):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pr(self):
        return (self.a + self.b) * 2


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return self.a * 4


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


class Oval(Geom):
    def __init__(self, a):
        self.a = a


rec = Rect(1, 2)
sq = Square(3)
tr = Triangle(4, 5, 6)
ov = Oval(7)

lst = [rec, sq, tr, ov]
for item in lst:
    print(item.get_pr())
