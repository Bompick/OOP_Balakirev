class Geom:
    name = "Geom"

    def draw(self):
        print('рисую форму')
    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.draw()



class Rect(Geom):
    name = "Rect"

    def draw(self):
        print('рисую прямоугольник')


class Line(Geom):
    name = "Line"

    def draw(self):
        print("рисую линию")


r = Rect()
l = Line()
g = Geom()
l.set_coords(1, 1, 2, 2)
r.set_coords(3, 3, 4, 4)
g.set_coords(5,5,6,6,)
print(l.__dict__)


