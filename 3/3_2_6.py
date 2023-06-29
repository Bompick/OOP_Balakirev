from string import digits


class DigitRetrieve:
    def __init__(self):
        self.chars = digits+'-'

    def __call__(self, string: str, *args, **kwargs):
        if set(string) <= set(self.chars):
            if "-" in string:
                if string.count('-') !=1 or string.find('-')!= 0:
                    return None
            return int(string)
        else:
            return None

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))
print(digits)