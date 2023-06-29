class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []
        self.curr_weight = 0

    def add_thing(self, thing):
        if self.curr_weight + thing.weight <= self.max_weight:
            self.bag.append(thing)
            self.curr_weight += thing.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item):
        if self.check_indx(item):
            return self.bag[item]

    def __setitem__(self, key, value):
        if self.check_indx(key):
            if self.curr_weight - self[key].weight + value.weight <= self.max_weight:
                self.bag[key] = value
                self.curr_weight = sum(map(lambda x: x.weight, self.bag))
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        if self.check_indx(key):
            del self.bag[key]
            self.curr_weight = sum(map(lambda x: x.weight, self.bag))

    def check_indx(self, val):
        if val < len(self.bag):
            return True
        else:
            raise IndexError('неверный индекс')

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
