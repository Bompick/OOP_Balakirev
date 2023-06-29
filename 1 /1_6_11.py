class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq


ld = Loader()
s = "4, 5, -6.5"
res = ld.parse_format(s, Factory())  # out: [4.0, 5.0, -6.5]
print(res)