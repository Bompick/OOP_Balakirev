class PathLines:
    X_START = 0
    Y_START = 0

    def __init__(self, *args):
        self.route = [i for i in args]

    def get_path(self):
        return self.route if len(self.route) > 0 else []


    def get_length(self):
        ttl_lenght = 0
        for i, j in enumerate(self.route):
            if i == 0:
                lenght = (((j.x-self.X_START)**2)+((j.y-self.Y_START)**2))**0.5
            else:
                lenght = (((j.x-self.route[i-1].x)**2)+((j.y-self.route[i-1].y)**2))**0.5
            ttl_lenght += lenght
        return ttl_lenght

    def add_line(self, line):
        self.route.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(1, 2))

p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []