import time


class Mechanical:
    name = 'mechanical'

    def __init__(self, date):
        self.date = int(date)

    def __setattr__(self, key, value):
        if len(self.__dict__) == 0 and  value > 0:
            object.__setattr__(self, key, value)


class Aragon:
    name = 'aragon'

    def __init__(self, date):
        self.date = int(date)

    def __setattr__(self, key, value):
        if len(self.__dict__) == 0 and  value > 0:
            object.__setattr__(self, key, value)


class Calcium:
    name = 'calcium'

    def __init__(self, date):
        self.date = int(date)

    def __setattr__(self, key, value):
        if len(self.__dict__) == 0 and  value > 0:
            object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    slot_names = {1: ('slot_1', 'mechanical'), 2: ('slot_2', 'aragon'), 3: ('slot_3', 'calcium')}

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num in self.slot_names and \
                getattr(self, self.slot_names[slot_num][0]) is None and \
                self.slot_names[slot_num][1] == filter.name:
            setattr(self, self.slot_names[slot_num][0], filter)

    def remove_filter(self, slot_num):
        if getattr(self, self.slot_names[slot_num][0]):
            setattr(self, self.slot_names[slot_num][0], None)

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        is_filled = (self.slot_1, self.slot_2, self.slot_3)
        if None in is_filled:
            return False
        expiration_list = []
        for i in is_filled:
            expiration_list.append(i.date)
        not_expired = all(map(lambda x: 0 <= (time.time()-x) <= self.MAX_DATE_FILTER, expiration_list))
        if not_expired is True:
            return True
        else:
            return False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть " \
                                                                                          "устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"