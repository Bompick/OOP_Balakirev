
class TupleLimit(tuple):
    def __new__(cls, lst, max_length,  *args, **kwargs):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __repr__(self):
        return ' '.join(str(i) for i in self)


digits = list(map(float, input().split()))
max_length = 5
try:
    tl = TupleLimit(digits, max_length)
except (ValueError, TypeError) as e:
    print(e)
else:
    print(tl)




