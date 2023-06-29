class Singleton:
    _is_inst = None
    _is_inst_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._is_inst_base is None:
                cls._is_inst_base = super().__new__(cls)
            return cls._is_inst_base
        if cls._is_inst is None:
            cls._is_inst = super().__new__(cls)
        return cls._is_inst


class Game(Singleton):
    _is_name = None

    def __init__(self, name):
        if self._is_name is None:
            self.name = name
            self._is_name = name


a = Singleton()
c = Game('1')
d = Game('2')
