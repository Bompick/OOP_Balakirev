class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, val1, val2):
        if isinstance(self, CellInteger) or isinstance(self, CellFloat):
            self._min_value = val1
            self._max_value = val2
            self._value = None
        elif isinstance(self, CellString):
            self._min_length = val1
            self._max_length = val2
            self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(self, CellInteger) and not self._min_value <= val <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        elif isinstance(self, CellFloat) and not self._min_value <= val <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        elif isinstance(self, CellString) and not self._min_length <= len(val) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = val


class CellInteger(Cell):
    pass


class CellFloat(Cell):
    pass


class CellString(Cell):
    pass


class TupleData:
    def __init__(self, *args):
        self.massive = args

    def __getitem__(self, item):
        self.check_len(item)
        return self.massive[item].value

    def __setitem__(self, key, value):
        self.check_len(key)
        self.massive[key].value = value

    def __len__(self):
        return len(self.massive)

    def __iter__(self):
        return iter([item.value for item in self.massive])

    def check_len(self, value):
        if not 0 <= value <= len(self):
            raise IndexError


t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
    CellStringException,
    CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"