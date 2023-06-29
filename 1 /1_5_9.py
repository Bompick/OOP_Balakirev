class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return list(map(lambda s: f'{s.name}:{s.price}',self.goods))

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price  = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
lst=[(TV("LG",120)),(TV("SS",100)), (Table("Keram",10)), (Notebook("MSI",99)), (Notebook("HP",58)), (Cup("Q",1))]
for item in lst:
    cart.add(item)

#cart.add(TV("LG",120))
#cart.add(TV("SS",100))
#cart.add(Table("Keram",10))
#cart.add(Notebook("MSI",99))
#cart.add(Notebook("HP",58))
#cart.add(Cup("Q",1))

