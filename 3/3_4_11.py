class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, table, *args, **kwargs):
        if not self.check_table(table):
            raise ValueError("Неверный формат для первого параметра matrix.")
        return self.find_max(table, self.size, self.step)

    @staticmethod
    def check_table(tab):
        if not type(tab) is list:
            return False
        b = list(map(len, tab))
        try:
            for k, l in enumerate(b):
                if b[k] != b[k+1]:
                    return False
        except IndexError:
            pass
        for col in tab:
            for i in col:
                if type(i) not in (int, float):
                    return False
        return True

    @staticmethod
    def find_max(table, size, step):
        new = []
        fin = []
        z = 0
        q = 0
        while True:
            s = []
            for i in range(0 + z * step[1], size[0] + z * step[1]):
                for j in range(0 + q * step[0], size[1] + q * step[0]):
                    try:
                        s.append(table[i][j])
                    except IndexError:
                        break
            if len(s) == size[0] * size[1]:
                new.append(max(s))
                q += 1
            else:
                if len(new) != 0:
                    fin.append(new)
                    z += 1
                    j = q = 0
                    s = new = []
                else:
                    return fin


mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
