class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def check_index(self, val):
        if 0 <= val < len(self.__dict__):
            return True
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        if self.check_index(item):
            return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        if self.check_index(key):
            self.__dict__[list(self.__dict__.keys())[key]] = value

    def __iter__(self):
        return iter(list(self.__dict__.values()))


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
print(pers.__dict__)
for v in pers:
    print(v)

