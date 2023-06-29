class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push_back(self, obj):
        if self.top is None:
            self.add_1st_block(obj)
        else:
            self.bottom.next = obj
            self.bottom = obj

    def push_front(self, obj):
        if self.top is None:
            self.add_1st_block(obj)
        else:
            temp = self.top
            self.top = obj
            self.top.next = temp

    def add_1st_block(self, obj):
        self.top = obj
        self.bottom = obj

    def __len__(self):
        temp = self.top
        counter = 1
        while temp.next:
            temp = temp.next
            counter += 1
        return counter

    def __iter__(self):
        temp = self.top
        while temp.data:
            yield temp
            temp = temp.next
            if temp is None:
                break


    def __setitem__(self, key, value):
        if self.check_indx(key):
            t = self.__iter__()
            for i in range(key+1):
                if i == key:
                    next(t).data = value
                    break
                next(t)


    def __getitem__(self, item):
        if self.check_indx(item):
            t = self.__iter__()
            for i in range(item+1):
                if i == item:
                    return next(t).data
                next(t)

    def check_indx(self, ind):
        if 0 <= ind < len(self):
            return True
        else:
            raise IndexError('неверный индекс')


st = Stack()
st.push_back(StackObj('1st'))
st.push_back(StackObj('2nd'))
st.push_back(StackObj('3rd'))
st.push_front(StackObj("New 1st"))



print(st[0])
st[2] = 'новый первый'
for obj in st:
    print(obj.data, end=' ')
