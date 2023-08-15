class Rect:
    def __init__(self, x, y, width, height):
        if type(x) not in (int, float) or type(y) not in (int, float) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        if not(self._y > rect._y + rect._height or self._y + self._height < rect._y \
        or self._x +self._width < rect._x or self._x > rect._x + rect._width):

            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for i in range(len(lst_rect)):
    counter = 0
    for j in range(len(lst_rect)):
        if i != j:
            try:
                lst_rect[i].is_collision(lst_rect[j])
                continue
            except TypeError:
                counter += 1
                break
    if counter == 0:
        lst_not_collision.append(lst_rect[i])


r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"
r2 = Rect(1.0, 2, 10.5, 20)
try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"

assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"

assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
