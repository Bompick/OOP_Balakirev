class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, obj):
        if self.bottom:
            self.bottom.next = obj
            self.bottom = obj
        if self.top is None:
            self.top = obj
            self.bottom = obj

    def pop(self):
        if self.bottom is None and self.top is None:
            return
        if self.bottom == self.top:
            prom = self.top
            self.top = None
            self.bottom = None
            return prom
        else:
            temp = self.top
            while temp.next != self.bottom:
                temp = temp.next
            prom = self.bottom
            self.bottom = temp
            self.bottom.next = None
            return prom

    def __getitem__(self, item):
        self.check(item)
        temp = self.top
        counter = 0
        if item == 0:
            return temp
        while counter < item:
            temp = temp.next
            counter += 1
            if temp.next is None:
                raise IndexError('неверный индекс')
        if counter <= item:
            return temp
        else:
            raise IndexError("Вы вышли за пределы")

    def __setitem__(self, key, value):
        if key == 0:
            temp = self.top.next
            self.top.next = None
            value.next = temp
            self.top = value
        temp = self.top
        counter = 0
        min = key - 1
        max = key + 1
        while counter != max:
            if counter == min:
                temp_low = temp
            temp = temp.next
            counter += 1
        if temp is not None:
            temp_low.next = value
            value.next = temp
        else:
            temp_low.next = value
            self.bottom = value

    @classmethod
    def check(cls, val):
        if not isinstance(val, int):
            raise IndexError('неверный индекс')


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"