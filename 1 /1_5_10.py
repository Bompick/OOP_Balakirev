class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj


lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

head_obj = ListObject(lst_in[0])
objs = [ListObject(lst_in[i]) for i in range(1, len(lst_in))]
objs.insert(0, head_obj)
for i in range(len(objs) - 1):
    objs[i].link(objs[i + 1])

assert isinstance(head_obj, ListObject) and hasattr(ListObject, 'link')

lst_data = []
h = head_obj
while h:
    lst_data.append(h.data)
    h = h.next_obj

assert lst_in == lst_data, "данные в объектах ListObject не совпадают с прочитанными данными (списком lst_in)"



