class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.route = []

    def add_track(self, tr):
        self.route.append(tr)

    def get_tracks(self):
        return tuple(self.route)

    def __len__(self):
        l1 = 0
        lst = [(item.to_x, item.to_y) for item in self.route]
        lst.insert(0, (self.start_x, self.start_y))
        for i, j in enumerate(lst):
            if i != 0:
                l_prom = ((j[0] - lst[i-1][0])**2 + (j[1] - lst[i-1][1])**2)**0.5
                l1 += l_prom
        return round(l1)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
print(len(track1))
print(len(track2))
print(track1 == track2)



