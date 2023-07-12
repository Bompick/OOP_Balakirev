class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        return type(value) is float and self.min_value <= value <= self.max_value


float_validator = FloatValidator(0, 10.5)
print(float_validator(1))
print(float_validator(1.0))
print(float_validator(-1.0))



