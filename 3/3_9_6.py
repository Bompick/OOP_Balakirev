class Person:
    def __init__(self, fio, job, old, salary, year_job ):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        if self.check(item):
            return self.temp()[item][-1]

    def __setitem__(self, key, value):
        if self.check(key):
            setattr(self, self.temp()[0][0], value)

    def temp(self):
        return [[key, value] for key, value in self.__dict__.items()]

    def __iter__(self):
        return iter([item[-1] for item in self.temp()])

    def check(self, val):
        if val in range(len(self.__dict__)):
            return True
        else:
            raise IndexError('неверный индекс')

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
