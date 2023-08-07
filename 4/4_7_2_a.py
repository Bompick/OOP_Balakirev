class Point2D:
    __slots__ = ('x', 'y',)

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ('z',)


pt3 = Point3D(10, 20)
pt3.z = 50
del pt3.x
pt3.x = 9
print(pt3.x)




