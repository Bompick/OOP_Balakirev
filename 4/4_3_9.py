class SoftList(list):
    def __getitem__(self, item):
        if self._check_value(item):
            return super().__getitem__(item)
        else:
            return False

    def __setitem__(self, key, value):
        if self._check_value(key):
            return super().__getitem__(key)
        else:
            return False


    def _check_value(self, value):
        if value >= 0 and value >= len(self) or value < 0 and value < -len(self):
            return False
        else:
            return True




sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False