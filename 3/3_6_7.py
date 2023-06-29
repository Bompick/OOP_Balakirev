
class ShopItem:
    def __init__(self, name, weight, price ):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = ['Системный блок: 1500 75890.56',
              'Монитор Samsung: 2000 34000',
              'Клавиатура: 200.44 545',
              'Монитор Samsung: 2000 34000']
shop_items = {}
for item in lst_in:
        new_data = item.split(':')
        p1 = new_data[0]
        p2 = new_data[-1].split()
        p2.insert(0, p1)
        obj = ShopItem(*p2)
        ttl =1
        if obj in shop_items:
            shop_items[obj][-1] += 1
        else:
            shop_items[obj] = [obj, ttl]

print(shop_items)


