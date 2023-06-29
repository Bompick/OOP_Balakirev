class Dimensions:
    def __init__(self, a, b, c):
        if self.check_value(a) and self.check_value(b) and self.check_value(c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")


    def __hash__(self):
        return hash((self.a, self.b, self.c))

    @staticmethod
    def check_value(value):
        return type(value) in (int, float) and value <=0


lst_dims=[]
s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
spl = s_inp.split("; ")
for item in spl:
    data = [float(i) if '.' in i else int(i) for i in item.split()]
    lst_dims.append(Dimensions(*data))


lst_dims.sort(key=lambda x: hash(x))





