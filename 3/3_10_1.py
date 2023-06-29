import random
class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple([tuple([Cell() for j in range(3)])for i in range(3)])
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value):
        self.__is_human_win = value

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value):
        self.__is_computer_win = value

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value):
        self.__is_draw = value


    @classmethod
    def check_index(cls, value):
        if all(map(lambda x: type(x) is int, value)) and all(map(lambda x: 0 <= x <= 2, value)):
            return True
        else:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        if self.check_index(item):
            row, col = item
            return self.pole[row][col].value

    def __setitem__(self, key, value):
        if self.check_index(key):
            row, col = key
            self.pole[row][col].value = value

    def __iter__(self):
        return iter(self.pole)

    def __bool__(self): # надо дописать условие
        if any(map(lambda x: x == 0, [item.value for row in self for item in row])) and self.__is_human_win is False and self.__is_computer_win is False and self.__is_draw is False :
            return True
        else:
            self.is_draw = True
            return False

    def init(self):
        for row in self.pole:
            for item in row:
                item.value = 0
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def show(self):
        for row in self:
            for item in row:
                print(item.value, end=' ')
            print()
        print()

    def human_go(self):
        if bool(self):
            row, col = map(int, input("Введите координаты через пробел").split())
            if self[row, col] == 0:
                self[row, col] = self.HUMAN_X
                self.check_winner(self.HUMAN_X)
            else:
                print("Эта клетка уже занята,  введите новые координаты")
                self.human_go()

    def computer_go(self):
        if bool(self):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self[row, col] == 0:
                self[row, col] = self.COMPUTER_O
                self.check_winner(self.COMPUTER_O)
            else:
                self.computer_go()

    def cur_pole(self):
        cur_pole = [item.value for row in self for item in row]
        r0 = cur_pole[:3]
        r1 = cur_pole[3:6]
        r2 = cur_pole[6:]
        c1 = cur_pole[::3]
        c2 = cur_pole[1::3]
        c3 = cur_pole[2::3]
        d1 = cur_pole[::4]
        d2 = cur_pole[2:7:2]
        return r0, r1, r2, c1, c2, c3, d1, d2

    def check_winner(self, value):
        pole = self.cur_pole()
        for item in pole:
            winner = []
            for val in item:
                if val != value:
                    break
                else:
                    winner.append(val)
            if len(winner) == 3 and value ==self.HUMAN_X:
                self.is_human_win = True
                break
            elif len(winner) == 3 and value ==self.COMPUTER_O:
                self.is_computer_win = True
                break

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"


game.show()
game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
game.show()
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"