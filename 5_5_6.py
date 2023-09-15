
class Box:
    def __init__(self, name, max_weight, current_weight=0, things=None):
        self._name = name
        self._max_weight = max_weight
        self._current_weight = current_weight
        if things is None:
            self._things = []
        else:
            self._things = things[:]

    def add_thing(self, obj: tuple):
        if self._current_weight + obj[-1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)
        self._current_weight += obj[-1]


class BoxDefender:
    def __init__(self, box: Box):
        self._box_for_check = box  # ссылка на коробку

    def __enter__(self):
        self._d_box = Box(self._box_for_check._name, self._box_for_check._max_weight, self._box_for_check._current_weight, self._box_for_check._things )
        return self._d_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._box_for_check._current_weight = self._d_box._current_weight
            self._box_for_check._things = self._d_box._things

        return False

b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"
b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"