class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    counter = 1

    def __init__(self, name,  weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__class__.counter
        self.__class__.counter += 1


    def get_id(self):
        return self.__id






item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")

print(item1.get_id())
print(item2.get_id())


