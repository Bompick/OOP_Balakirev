class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lst: list = []

    def __to_set_head_and_tale(self):
        if len(self.lst) > 0:
            self.head = self.lst[0]
            self.tail = self.lst[-1]

    def add_obj(self, obj):
        self.lst.append(obj)
        if len(self.lst) > 1:
            self.lst[len(self.lst)-2].set_next(obj)
            self.lst[len(self.lst) - 1].set_prev(self.lst[len(self.lst)-2])
        self.__to_set_head_and_tale()

    def remove_obj(self):
        if len(self.lst) >= 1:
            self.lst.pop()
            if len(self.lst) == 0:
                self.head = None
                self.tail = None
            else:
                self.lst[-1].set_next_none()
                self.__to_set_head_and_tale()

    def get_data(self):
        returned_data: list[str] = []
        for obj in self.lst:
            returned_data.append(obj.get_data())
        return returned_data


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next_none(self):
        self.__next = None


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))

lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)

ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
assert ls_one.get_data() == [1], "метод get_data вернул неверные данные"

h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
ls_one.remove_obj()
assert ls_one.get_data() == [], "метод get_data вернул неверные данные для пустого списка, возможно, неверно работает метод remove_obj"

ls2 = LinkedList()
assert ls.head != ls2.head, "атрибут head должен принадлежать объекту класса LinkedList, а не самому классу"
assert ls.tail != ls2.tail, "атрибут tail должен принадлежать объекту класса LinkedList, а не самому классу"

h = ls.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.head
n = 0
while h:
    h = h._ObjList__next
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __next"

h = ls.tail
n = 0
while h:
    n += 1
    h = h.get_prev()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.tail
n = 0
while h:
    h = h._ObjList__prev
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __prev"