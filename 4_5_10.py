class Track:
    def __init__(self, *args):
        if all(map(lambda x: type(x) in (int, float), args)) and len(args) == 2:
            a = list()
            a.append(PointTrack(*args))
            self.__points = a
        else:
            self.__points = [*args]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.x = x
            self.y = y
        else:
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        a = str(self.__class__).split('.')[-1][:-2]
        return f"{a}: {self.x}, {self.y}"


tr = Track(0, 0)
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)



