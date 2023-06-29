from string import digits


class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        chars = digits+"-"
        if set(string) <= set(chars):
            if "-" in string:
                if string.count('-') != 1 or string.find('-') != 0:
                    return None
            return int(string)
        else:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            inp_data_spl = func().split()
            res = list(map(self.render, inp_data_spl))
            return res
        return wrapper


a = InputValues(RenderDigit())
input_dg = a(input)
res = input_dg()
print(res)
