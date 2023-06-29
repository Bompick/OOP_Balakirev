class Tuple(tuple):
    def __add__(self, other):
        c = tuple(other)
        return Tuple(super().__add__(c))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)

