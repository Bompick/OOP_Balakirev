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
        if self._is_move and self._tp == 1:
            self._x += go
        elif self._is_move and self._tp == 2:
            self._y += go
        self.height_width()

    def is_collide(self, ship=None):
        if ship is None:
            return True

        self.height_width()
        ship.height_width()

        if (self._y == ship._y and self._x <= ship._x <= self._width or
                self._x == ship._x and self._y <= ship._y <= self._height):
            return True

        if self._y > ship._height + 1 or self._height + 1 < ship._y \
                or self._width + 1 < ship._x or self._x > ship._width + 1:
            return False
        else:
            return True

    def height_width(self):
        if self._tp == 1:
            self._height = self._y
            self._width = self._x + self._length - 1

        elif self._tp == 2:
            self._height = self._y + self._length - 1
            self._width = self._x

    def is_out_pole(self, size=10):
        if self._tp == 1:
            if self._x + self._length <= size - 1:
                return True
            else:
                return False

        elif self._tp == 2:
            if self._y + self._length <= size - 1:
                return True
            else:
                return False


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []


    # def init(self):
    #     for i in range(1, 5):
    #         temp = [Ship(5-i, tp=randint(1, 2)) for j in range(i)]
    #         self._ships.extend(temp)

    def init(self):
        self._ships = [Ship(5 - i, tp=randint(1, 2))
                       for i in range(1, 5)
                       for j in range(i)]

        for number, ship in enumerate(self._ships):
            while True:
                x, y = [randint(0, self._size - 1) for i in range(2)]
                temp_ship = Ship(ship._length, ship._tp, x, y)
                temp_ship.height_width()
                if temp_ship.is_out_pole() and self.check_of_collision(temp_ship):
                    ship.set_start_coords(x, y)
                    ship.height_width()
                    break
            print(f"My coords is {x, y},I'm {ship._cells}, tp={ship._tp}")


    def check_of_collision(self, ship_for_check):
        flot = [ship for ship in self._ships if ship._x is not None and ship._y is not None]
        if len(flot) == 0:
            return True

        temp_lst = []
        for boat in flot:
            if not ship_for_check.is_collide(boat):
                temp_lst.append(boat)

        if len(flot) == len(temp_lst):
            return True
        else:
            return False


    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        self.create_pole()
        for row in self._pole:
            for item in row:
                print(item, end=' ')
            print()
        self._pole = None
    def create_pole(self):
        self._pole = [[0 for i in range(self._size)]
                      for j in range(self._size)]

        for ship in self._ships:
            if ship._tp == 1:
                for i in range(len(ship._cells)):
                    self._pole[ship._y][ship._x+i] += ship._cells[i]
            elif ship._tp == 2:
                for i in range(len(ship._cells)):
                    self._pole[ship._y+i][ship._x] += ship._cells[i]



    def get_pole(self):
        return tuple(tuple(item) for item in self._pole)


# ship1=Ship(4,1,0,6)
# ship2=Ship(2,1,1,6)
# print(ship1.is_collide(ship2))

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
print()
pole.show()

