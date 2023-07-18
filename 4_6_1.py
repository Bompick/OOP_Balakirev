class Goods:
    def __init__(self, name, weight, price):
        print('init GOODS initializator')
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class Logger:
    ID = 0

    def __init__(self):
        print('init LOGGER')
        self.__class__.ID += 1
        self.id = self.__class__.ID

    def save_log(self):
        print(f'{self.id}: was sold at 12:00 PM')


class Notebook(Goods, Logger):
    pass



n = Notebook('Acer', 2, 30000)
n.print_info()
n.save_log()
print(Notebook.mro())
