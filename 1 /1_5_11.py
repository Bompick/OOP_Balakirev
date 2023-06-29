import random


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False


class GamePole:
    def init(self):
        pass

    def __init__(self, N: int, M: int, ):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(N)] for j in range(N)]

        for x in range(self.M):
            d = random.randint(0, N - 1)
            e = random.randint(0, N - 1)
            while getattr(self.pole[d][e], 'mine') is True:
                d = random.randint(0, N - 1)
                e = random.randint(0, N - 1)
                if getattr(self.pole[d][e], 'mine') is False:
                    break
            self.pole[d][e].mine = True
            for y in range(d - 1, d + 2):
                for z in range(e - 1, e + 2):
                    try:
                        if y == d and z == e or y < 0 or z < 0:
                            continue
                        self.pole[y][z].around_mines += 1
                    except IndexError:
                        continue
   

    def to_get_value(self, obj):
        if obj.fl_open == False:
            return "#"
        elif obj.fl_open == True and obj.mine == True:
            return "B"
        elif obj.fl_open == True and obj.mine == False:
            return obj.around_mines

    def show(self):
        for item in [[self.to_get_value(i) for i in j] for j in self.pole]:
            print(*item)


pole_game = GamePole(10,12)
print(pole_game.show())