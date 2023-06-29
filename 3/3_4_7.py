class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, value):
        self.__data = value

    def get_next(self):
        return self.__next

    def set_next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push_back(self, obj):
        if self.bottom:
            self.bottom.set_next(obj)
            self.bottom = obj
        if self.top is None:
            self.top = obj
            self.bottom = obj

    def pop_back(self):
        if self.bottom is None and self.top is None:
            return
        if self.bottom == self.top:
            self.top = None
            self.bottom = None
        else:
            temp = self.top
            while temp.get_next and temp.get_next() != self.bottom:
                temp = temp.get_next()
            self.bottom = temp
            self.bottom.set_next(None)

    def __add__(self, other):
        if not isinstance(other, StackObj):
            raise TypeError("Must be StackObj ")
        self.push_back(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, list):
            raise TypeError("Must be list ")
        for i in other:
            ob = StackObj(i)
            self.push_back(ob)
        return self


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
