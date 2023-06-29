class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for col in range(self.cols)] for row in range(self.rows)]

    def __getitem__(self, item):
        if self.check_index(item):
            return self.table[item[0]][item[1]].data

    def __setitem__(self, key, value):
        if self.check_index(key):
            if type(value) == self.type_data:
                self.table[key[0]][key[1]].data = value
            else:
                raise TypeError('неверный тип присваиваемых данных')

    def __iter__(self):
        return iter([[value.data for value in row] for row in self.table])

    def check_index(self, value):
        if all(map(lambda x: type(x) is int, value)) and 0 <= value[0] < self.rows and 0 <= value[1] < self.cols:
            return True
        else:
            raise IndexError('неверный индекс')


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"