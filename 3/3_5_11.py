class Thing:
    def __init__(self,name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


class Box:
    def __init__(self):
        self. vault = []

    def add_thing(self, obj):
        self.vault.append(obj)

    def get_things(self):
        return self.vault

    def __eq__(self, other):
        if len(self.vault) != len(other.vault):
            return False
        counter = 0
        for item in self.vault:
            for it in other.vault:
                if item == it:
                    counter += 1
        return True if counter == len(self.vault) else False

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 20000))

print(b1==b2)
