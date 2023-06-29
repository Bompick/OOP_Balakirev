class Clock:
    __DAY = 86400

    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise  TypeError("ВВеди целое число")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Бла")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds+sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print('Это я!!!')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Бла")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


c1 = Clock(15)
c1 += 105
print(c1.get_time())
