class FloatValue:

    @classmethod
    def to_check_float(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name ="" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.to_check_float(value)
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell() for _ in range(self.M)]for _ in range(self.N)]

    def to_add_value(self):
        values_list = list(range(1, int(self.N * self.M) + 1))
        for i, j in enumerate(self.cells):
            for k, l in enumerate(j):
                l.value = float(values_list[self.M*i + (0+k)])


table = TableSheet(5, 3)
table.to_add_value()

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3
assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
print(res)
assert res == list(range(1, 16))
table.cells[0][0].value = 1.0
x = table.cells[1][0].value
try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"