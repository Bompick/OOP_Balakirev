class Array:
    def __init__(self, max_length, cell):
        self.array = [cell() for i in range(max_length)]

    def __getitem__(self, item):
        if self.check_index(item):
            return self.array[item].value

    def __setitem__(self, key, value):
        if self.check_index(key):
            self.array[key].value = value

    def __str__(self):
        return ' '.join([str(item.value) for item in self.array])

    def check_index(self, value):
        if 0 <= value <= len(self.array)-1:
            return True
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if self.check(val):
            self.__value = val

    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        else:
            return True


a = Array(20, cell=Integer)
assert a[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

a = Array(2, cell=Integer)
a[0] = 1
a[1] = 2
assert str(a) == "1 2", "функция str(a) для объекта класса Array вернула неверное значение"
assert a[0] == 1 and a[1] == 2, "некорректно работает запись и/или считывание значений из массива по индексу"

try:
    a[1] = 2.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    a[100] = 25
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

