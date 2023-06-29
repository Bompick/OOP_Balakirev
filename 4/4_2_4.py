class ListInteger(list):
    def __init__(self, *data):
        self.check_data(data)
        super().__init__(data)

    def __setitem__(self, key, value):
        self.check_data(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.check_data(value)
        super().append(value)

    @staticmethod
    def check_data(value):
        if type(value) is int or all(map(lambda x: type(x) is int, value)):
            return True
        else:
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger(1, 2, 3)
s[1] = 10
s.append(11)
print(s)
#s[0] = 10.5 # TypeError