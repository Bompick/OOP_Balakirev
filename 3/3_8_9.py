class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple([tuple([Cell() for i in range(3)]) for j in range(3)])

    def clear(self):
        for i in self.pole:
            for j in i:
                j.value = 0
                j.is_free = True

    def __getitem__(self, item):
        if self.check(item):
            if any(map(lambda x: type(x) is slice, item)):
                if type(item[0]) is int:
                    return tuple((i.value for i in self.pole[item[0]]))
                else:
                    return tuple(j.value for row in self.pole for i, j in enumerate(row) if i == item[-1])

            else:
                return self.pole[item[0]][item[-1]].value

    def __setitem__(self, key, value):
        if self.check(key):
            if bool(self.pole[key[0]][key[-1]]):
                self.pole[key[0]][key[1]].value = value
                self.pole[key[0]][key[1]].is_free = False
            else:
                raise ValueError('клетка уже занята')

    @classmethod
    def check(cls, val):
        for i in val:
            if type(i) is int and i <3:
                continue
            elif type(i) is slice:
                continue
            else:
                raise IndexError('неверный индекс клетки')
        return True

g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"

g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"