class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        if self._check(item):
            return self.__dict__[list(self.__dict__.keys())[item]]

    def __setitem__(self, key, value):
        if self._check(key):
            self.__dict__[list(self.__dict__.keys())[key]] = value

    def _check(self, value):
        if type(value) is int and value < len(self.__dict__):
            return True
        else:
            raise IndexError('неверный индекс поля')


r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1])

