class Thing:
    counter = 0

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None ):
        self.id = __class__.counter
        __class__.counter += 1
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm


    def get_data(self):

        return tuple(self.__dict__.values())[:-1]

class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight=weight, dims=dims)


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())