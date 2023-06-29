class ObjList:
    def __init__(self, data):
        self.__prev = None
        self.__next = None
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


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        if self.head is None and self.tail is None:
            return
        if self.head:
            temp_head = self.head
            for i in range(indx):
                temp_head = temp_head.get_next()
            if indx == 0 and self.__len__()==1:
                self.tail = None
                self.head = None
                return
            if indx == 0:
                nextik = temp_head.get_next()
                temp_head = temp_head.get_next()
                prev = temp_head.get_prev()
                nextik.set_prev(None)
                prev.set_next(None)
                self.head = temp_head
                return

            if temp_head.get_next():
                prev = temp_head.get_prev()
                nextik = temp_head.get_next()
                prev.set_next(nextik)
                nextik.set_prev(prev)
            else:
                prev = temp_head.get_prev()
                temp_head.set_next(None)
                temp_head.set_prev(None)
                prev.set_next(None)
                self.tail = prev

    def __len__(self):
        if self.head:
            temp_head = self.head
            counter = 1
            while temp_head.get_next():
                temp_head = temp_head.get_next()
                counter += 1
            return counter

    def __call__(self, indx):
        if self.head:
            temp_head = self.head
            for i in range(indx):
                temp_head = temp_head.get_next()
            return temp_head.get_data()


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"