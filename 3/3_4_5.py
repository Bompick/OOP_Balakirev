class NewList:
    def __init__(self, lst=[]):
        self.lst = lst

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError("должен быть список")
        if isinstance(other, NewList):
            other = other.lst
        c1 = list(self.lst)
        c2 = list(other)
        lst_fin = []
        for i in c1:
            if i not in (0, 1, True, False) and i not in c2:
                lst_fin.append(i)
            elif i not in (0, 1, True, False) and i in c2:
                c2.remove(i)
            elif i in (0, 1, True, False) and i not in c2:
                lst_fin.append(i)
            elif i in (0, 1, True, False) and i in c2:
                for x in c2:
                    if x == i and type(x) == type(i):
                        c2.remove(i)
                        break
                    elif x == i and type(x) != type(i):
                        lst_fin.append(i)
        return NewList(lst_fin)
    def __rsub__(self, other):
        return NewList(other) - NewList(self.lst)



lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"