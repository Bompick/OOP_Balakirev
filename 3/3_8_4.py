class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def add_point(self, x, y, speed):

        self.track.append([(x, y), speed])

    def __getitem__(self, item):
        if self.check_index(item):
            return self.track[item][0], self.track[item][-1]

    def __setitem__(self, key, value):
        if self.check_index(key):
            self.track[key][-1] = value


    def check_index(self, value):
        if 0 <= value <= len(self.track)-1:
            return True
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)


