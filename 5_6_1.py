from random import randint, choice


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
        if self._is_move and self._tp == 1 and self._x + go >= 0:
            self._x += go
        elif self._is_move and self._tp == 2 and self._y + go >= 0:
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
                return False
            else:
                return True

        elif self._tp == 2:
            if self._y + self._length <= size - 1:
                return False
            else:
                return True


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []

    def init(self):
        self._ships = [Ship(5 - i, tp=randint(1, 2))
                       for i in range(1, 5)
                       for j in range(i)]

        for number, ship in enumerate(self._ships):
            while True:
                x, y = [randint(0, self._size - 1) for i in range(2)]
                temp_ship = Ship(ship._length, ship._tp, x, y)
                temp_ship.height_width()
                if not temp_ship.is_out_pole() and self.check_of_collision(temp_ship):
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
        for num, ship in enumerate(self._ships):
            temp_ship = Ship(ship._length, ship._tp, ship._x, ship._y)
            temp_ship.height_width()
            temp_ship2 = Ship(ship._length, ship._tp, ship._x, ship._y)
            temp_ship2.height_width()
            directions = [-1, 1]
            dir = choice(directions)
            directions.remove(dir)
            temp_ship.move(dir)

            if not temp_ship.is_out_pole() and self.check_for_collision_2(temp_ship, num):
                ship.set_start_coords(temp_ship._x, temp_ship._y)
                ship.height_width()
                print(f'я переместился {dir}')

            else:
                temp_ship2.move(directions[0])
                if not temp_ship.is_out_pole() and self.check_for_collision_2(temp_ship, num):
                    ship.set_start_coords(temp_ship._x, temp_ship._y)
                    ship.height_width()
                    print(f'переместился в {directions[0]}')
                else:
                    print('остался на месте')


    def check_for_collision_2(self, ship_for_check, number):
        flot = [ship for num, ship in enumerate(self._ships) if num != number]
        temp_lst = []
        for boat in flot:
            if not ship_for_check.is_collide(boat):
                temp_lst.append(boat)

        if len(flot) == len(temp_lst):
            return True
        else:
            return False

    def show(self):
        # self.create_pole()
        data = self.get_pole()
        for row in data:
            for item in row:
                print(item, end=' ')
            print()
        self._pole = None
    # def create_pole(self):
    #     self._pole = [[0 for i in range(self._size)]
    #                   for j in range(self._size)]
    #
    #     for ship in self._ships:
    #         if ship._tp == 1:
    #             for i in range(len(ship._cells)):
    #                 self._pole[ship._y][ship._x+i] += ship._cells[i]
    #         elif ship._tp == 2:
    #             for i in range(len(ship._cells)):
    #                 self._pole[ship._y+i][ship._x] += ship._cells[i]



    def get_pole(self):
        self._pole = [[0 for i in range(self._size)]
                      for j in range(self._size)]

        for ship in self._ships:
            if ship._tp == 1:
                for i in range(len(ship._cells)):
                    self._pole[ship._y][ship._x+i] += ship._cells[i]
            elif ship._tp == 2:
                for i in range(len(ship._cells)):
                    self._pole[ship._y+i][ship._x] += ship._cells[i]

        return tuple(tuple(item) for item in self._pole)


# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
#
# pole.move_ships()
# print()
# pole.show()
# # ship1  = Ship(3,1,0,9)
# # ship1.move(-1)
# # print('1')

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"
ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()