class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'{self.__class__.__name__}'


data = [1,2]

try:
    x, y = map(int, data)
    pt = Point(x, y)
except ValueError:
    try:
        x, y = map(float, data)
        pt = Point(x, y)
    except ValueError:
        pt = Point()
finally:
    print(f'{pt}: x = {pt._x}, y = {pt._y}')
















