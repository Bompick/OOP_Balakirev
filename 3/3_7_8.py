class Ellipse:
    def __init__(self, *args):
        if len(args) > 0:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]
        else:
            pass

    def __bool__(self):
        return True if self.__dict__ else False

    def get_coords(self):
        if self.__bool__():
            return tuple(self.__dict__.values())
        else:
            raise AttributeError('нет координат для извлечения')


el1 = Ellipse()
el2 = Ellipse(1, 1, 2, 2)

lst_geom =[Ellipse(), Ellipse(), Ellipse(1,2,3,4), Ellipse(5,6,7,8)]
for item in lst_geom:
    if bool(item):
        item.get_coords()
