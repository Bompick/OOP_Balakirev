class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.check_value(value):
            instance.__dict__[self.name] = value

    @staticmethod
    def check_value(val):
        if isinstance(val,int):
            return True
        else:
            raise ValueError('возможны только целочисленные значения')

class CellInteger:
    value = IntegerValue()

    def __init__(self, value=0):
        self.value = value


class TableValues:
    def __init__(self, rows, cols, **kwargs):
        if "cell" not in kwargs:
            raise ValueError('параметр cell не указан')
        self.cells = tuple([tuple([kwargs['cell']() for i in range(cols)]) for j in range(rows)])

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value


table = TableValues(2, 3, cell=CellInteger)

table[1, 1] = 10

for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
