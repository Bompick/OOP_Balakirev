class PolyLine:
    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.coords = list(args)
        self.ttl_coords = self.coords.insert(0, self.start_coord)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords



a = PolyLine((1, 2), (5, 9), (15, 19))
print(a.get_coords())