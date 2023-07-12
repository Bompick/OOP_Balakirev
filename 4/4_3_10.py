class StringDigit(str):
    def __init__(self, data):
        if self.check_value(data):
            super().__init__()

    def __add__(self, other):
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(other)+self



    @staticmethod
    def check_value(value):
        if all(map(lambda x: x.isdigit(), value)):
            return True
        else:
            raise ValueError("в строке должны быть только цифры")


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
print(sd)
sd = sd + "12f"
