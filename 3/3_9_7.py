import random


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.counter = -1

    def __iter__(self):
        return iter([x for row in self.lst for x in row])

    def __next__(self):
        self.counter += 1
        prom = []
        for row in range(self.counter, len(self.lst[self.counter])):
            for x in range(0, len(self.lst[self.counter]-1)):
                prom.append(self.lst[row][x])
        return prom





lst = [['x00', 'x01', 'x02'],
       ['x10','x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)
it_iter = iter(it)
print(next(it))
print(next(it))

