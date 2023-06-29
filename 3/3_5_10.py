class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.mas = ro * volume

    def __eq__(self, other):
        if isinstance(other, Body):
            other = other.mas
        return self.mas ==  other

    def __lt__(self, other):
        if isinstance(other, Body):
            other = other.mas
        return self.mas < other



body1 = Body('1', 5, 20)
body2 = Body('2', 4, 20)
print(body1 > body2)
