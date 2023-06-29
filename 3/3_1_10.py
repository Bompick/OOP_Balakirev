class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    attrs = ['a', 'b', 'c', 'MIN_DIMENSION', 'MAX_DIMENSION' ]

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return object.__getattribute__(self, "__a")

    @a.setter
    def a(self, value):
        object.__setattr__(self, "__a", value)

    @property
    def b(self):
        return object.__getattribute__(self, "__b")

    @b.setter
    def b(self, value):
        object.__setattr__(self, "__b", value)

    @property
    def c(self):
        return object.__getattribute__(self, "__c")

    @c.setter
    def c(self, value):
        object.__setattr__(self, "__c", value)

    def __setattr__(self, key, value):
        if key in self.attrs[0:3] and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)
        elif key in self.attrs[3:]:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            return


d = Dimensions(10.5, 20.1, 30)


