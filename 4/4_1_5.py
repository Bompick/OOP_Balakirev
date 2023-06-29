class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def get_info(self):
        if isinstance(self, Cat):
            return f'{self.name}: {self.old}, {self.color}, {self.weight}'
        elif isinstance(self, Dog):
            return  f'{self.name}: {self.old}, {self.breed}, {self.size}'

class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size



cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())




