class Furniture:
    def __init__(self, name, weight):
        if self.__verify_name(name):
            self._name = name
        if self.__verify_weight(weight):
            self._weight = weight

    @staticmethod
    def __verify_name(value):
        if type(value) is not str:
            raise TypeError('название должно быть строкой')
        else:
            return True

    @staticmethod
    def __verify_weight(value):
        if type(value) not in (int, float) and value <= 0:
            raise TypeError('вес должен быть положительным числом')
        else:
            return True


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
