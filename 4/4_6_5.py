class Digit:
    def __init__(self, value):
        if type(value) in (int, float):
            self.value = value
        else:
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        if type(value) is int:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        if type(value) is float:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        if value > 0:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        if value < 0:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))




