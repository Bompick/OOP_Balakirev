class Validator:
    def __init__(self, min_value, max_value):
        self._min = min_value
        self._max = max_value

    def __call__(self, value):
        if type(self) is FloatValidator:
            if type(value) is not float or value < self._min or value > self._max:
                raise ValueError('значение не прошло валидацию')

        elif type(self) is IntegerValidator:
            if type(value) is not int or value < self._min or value > self._max:
                raise ValueError('значение не прошло валидацию')

        return True


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def __call__(self, value):
        if super().__call__(value):
            return value


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def __call__(self, value):
        super().__call__(value)
        return value

#
# def is_valid(lst, validators):
#     to_return = []
#     for item in validators:
#         for it in lst:
#             try:
#                 val = item(it)
#                 if val not in to_return:
#                     to_return.append(val)
#             except ValueError:
#                 pass
#     return to_return

def is_valid(lst, validators):
    to_return = []
    for item in lst:
        for it in validators:
            try:
                val = it(item)
                if val not in to_return:
                    to_return.append(val)
            except ValueError:
                pass
    return to_return


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2), 10, 0.5], validators=[fv, iv])
print(lst_out)