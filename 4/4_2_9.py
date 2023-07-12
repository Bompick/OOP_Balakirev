class IteratorAttrs:
    def __iter__(self):
        #return iter(self.__dict__.items())
        for x in self.__dict__.items():
            yield x


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone("GalaxyS10", "1980*720", '4Gb')
for attr, value in phone:
    print(attr, value)
    print()


