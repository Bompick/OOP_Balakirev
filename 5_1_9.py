lst_in = "1 -5.6 True abc 0 23.56 hello"
lst_in = lst_in.split()

def check(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(check, lst_in))
