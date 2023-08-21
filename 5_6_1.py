from random import randint
class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for i in range(self._length)]

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        pass  # прописать функцию

    def is_collide(self, ship):
        pass  # прописать функцию

    def is_out_pole(self, size):
        pass  # прописать функцию


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []


    def init(self):
        for i in range(1, 5):
            temp = [Ship(5-i, tp=randint(1, 2)) for j in range(i)]
            self._ships.extend(temp)



    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        pass

    def get_pole(self):
        pass



ship = Ship(4)
pole = GamePole()
pole.init()
