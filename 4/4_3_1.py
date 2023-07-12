class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom  для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('рисую линию')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        print('инициализвтор Rect')
        super().__init__(x1, y1, x2, y2)
        self.fill = fill

    def draw(self):
        print('рисую прямоуголник')


# l1 = Line(1, 1, 2, 2)
r1 = Rect(3, 3, 4, 4)
