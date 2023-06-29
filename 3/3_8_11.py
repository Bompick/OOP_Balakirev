class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}

    def add_data(self, row, col, data):
        if (row, col) not in self.table:
            self.table[(row, col)] = data
            self.rows, self.cols = self.calc()

    def remove_data(self, row, col):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.table[(row, col)]
        self.rows, self.cols = self.calc()

    def __getitem__(self, item):
        if item not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table[item]

    def __setitem__(self, key, value):
        self.table[key] = value
        self.rows, self.cols = self.calc()

    def calc(self):
        row = max([item[0] for item in self.table.keys()])+1
        col = max([item[1] for item in self.table.keys()])+1
        return row, col

st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"