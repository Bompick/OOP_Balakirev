lst_in = "8 11 abcd -7.5 2.0 -5"
lst_in = lst_in.split()

def check(value):
    try:
        return int(value)
    except:
        pass


a = sum(list(map(int, filter(check, lst_in))))
print(a)
