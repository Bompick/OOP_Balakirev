class Note:
    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton


    def __setattr__(self, key, value):
        if key == '_ton' and value not in range(-1, 2) \
            or key == "_name " and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        else:
            self.__dict__[key] = value


class Notes:
    __isinstance = None
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    RUS_NOTES = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)
        return cls.__isinstance

    def __init__(self):
        for num, note in enumerate(self.__class__.__slots__):
            setattr(self, note, Note(self.__class__.RUS_NOTES[num]))

    def __getitem__(self, item):
        if self.check_value(item):
            return getattr(self, self.__class__.__slots__[item])

    def __setitem__(self, key, value):
        if self.check_value(key):
            obj = getattr(self, self.__class__.__slots__[key])
            obj._ton = value

    def check_value(self, value):
        if 0 <= value < len(self.__class__.__slots__):
            return True
        else:
            raise IndexError('недопустимый индекс')


notes = Notes()
nota = notes[2]
notes[3]._ton = -1



