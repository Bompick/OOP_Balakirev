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
                q = c2.count(i)
                prom = []
                for y, x in enumerate(c2):

                    if x == i and type(x) == type(i):
                        c2.pop(y)
                        break
                    elif x == i and type(x) != type(i):
                        prom.append(x)
                if len(prom) == q and all(map(lambda x: type(x), prom)):
                    lst_fin.append(i)

        return NewList(lst_fin)

    def __rsub__(self, other):
        return NewList(other) - NewList(self.lst)


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] \
       and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"