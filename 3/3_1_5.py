class Shop:
    def __init__(self, name: str):
        self.name = name
        self.goods: list = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        for item in self.goods:
            if item.id == product.id:
                self.goods.remove(product)


class Product:
    id_to_set = 0

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.to_set_id()

    @classmethod
    def to_set_id(cls):
        cls.id_to_set += 1
        return cls.id_to_set

    def __setattr__(self, key, value):
        if key == 'name' and type(value) is not str or \
                key in ('weight', 'price') and type(value) not in (int, float) or \
                key in ('weight', 'price') and value < 0 or\
                key == 'id' and type(value) is not int and value < 1:

            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            super.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super.__delattr__(self, item)


p = Product('', -1, -2)


