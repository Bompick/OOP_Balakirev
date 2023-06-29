import random

class GamePole:
    _isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls._isinstance is None:
            cls._isinstance = super().__new__(cls)
        return cls._isinstance

    def __init__(self, N, M,total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple([tuple([Cell() for i in range(M)]) for j in range(N)])

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        counter = 0
        while counter < self.total_mines:
            a = random.randint(0, self.N-1)
            b = random.randint(0, self.M-1)
            mine = self.pole[a][b]
            if mine.is_mine is False:
                mine.is_mine = True
                counter += 1
                for x in range(a-1, a+2):
                    for y in range(b-1, b+2):
                        if x== -1 or y == -1:
                            continue
                        try:
                            if a==x and b==y:
                                continue
                            if self.pole[x][y].is_mine is False:
                                self.pole[x][y].number += 1
                        except:
                            pass
            else:
                continue


    def open_cell(self, i, j):
        scope: Cell = self.pole[i][j]
        scope.is_open = True


    def show_pole(self):
        for col in self.pole:
            for item in col:
                if not item.is_open:
                    print("X", end=' ')
                else:
                    if item.is_mine:
                        print("*", end=' ')
                    else:
                        print(item.number, end=' ')
            print("")





class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open  = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if self.check_bool(is_mine):
            self.__is_mine = is_mine

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if self.check_int(number):
            self.__number = number

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if self.check_bool(is_open):
            self.__is_open = is_open

    @classmethod
    def check_bool(cls, val):
        if type(val) is bool:
            return True
        else:
            raise ValueError("недопустимое значение атрибута")

    @classmethod
    def check_int(cls, val):
        if type(val) is int and 0 <= val <=8:
            return True
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        if self.is_open:
            return False
        else:
            return True

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n

for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"