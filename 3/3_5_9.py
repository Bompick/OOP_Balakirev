class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume == actual \
                        or self.volume == actual - 0.1 \
                        or self.volume == actual + 0.1 else False

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume < actual \
                        or self.volume < actual - 0.1 \
                        or self.volume < actual + 0.1 else False

    def __le__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume <= actual \
                        or self.volume <= actual - 0.1 \
                        or self.volume <= actual + 0.1 else False

    def __gt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume > actual \
                        or self.volume > actual - 0.1 \
                        or self.volume > actual + 0.1 else False

    def __ge__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume >= actual \
                        or self.volume >= actual - 0.1 \
                        or self.volume >= actual + 0.1 else False

    @staticmethod
    def calc(other):
        if isinstance(other, MoneyD):
            ex = other.cb.rates['rub']
        elif isinstance(other, MoneyE):
            ex = other.cb.rates['rub'] * other.cb.rates['euro']
        elif isinstance(other, MoneyR):
            ex = 1
        return round(ex * other.volume, 1)


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume == actual \
                        or self.volume == actual - 0.1 \
                        or self.volume == actual + 0.1 else False


    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume < actual \
                        or self.volume < actual - 0.1 \
                        or self.volume < actual + 0.1 else False

    def __le__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume <= actual \
                        or self.volume <= actual - 0.1 \
                        or self.volume <= actual + 0.1 else False

    def __gt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume > actual \
                        or self.volume > actual - 0.1 \
                        or self.volume > actual + 0.1 else False

    def __ge__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume >= actual \
                        or self.volume >= actual - 0.1 \
                        or self.volume >= actual + 0.1 else False

    @staticmethod
    def calc(other):
        if isinstance(other, MoneyE):
            ex = other.cb.rates['euro']
        elif isinstance(other, MoneyR):
            ex = other.cb.rates['dollar'] / other.cb.rates['rub']
        elif isinstance(other, MoneyD):
            ex = 1
        return round(ex * other.volume, 1)

class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume == actual \
                        or self.volume == actual - 0.1 \
                        or self.volume == actual + 0.1 else False


    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume < actual \
                        or self.volume < actual - 0.1 \
                        or self.volume < actual + 0.1 else False

    def __le__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume <= actual \
                        or self.volume <= actual - 0.1 \
                        or self.volume <= actual + 0.1 else False

    def __gt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume > actual \
                        or self.volume > actual - 0.1 \
                        or self.volume > actual + 0.1 else False

    def __ge__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        actual = self.calc(other)
        return True if self.volume >= actual \
                        or self.volume >= actual - 0.1 \
                        or self.volume >= actual + 0.1 else False

    @staticmethod
    def calc(other):
        if isinstance(other, MoneyD):
            ex = other.cb.rates['dollar'] / other.cb.rates['euro']
        elif isinstance(other, MoneyR):
            ex = other.cb.rates['dollar'] / other.cb.rates['rub'] / other.cb.rates['euro']
        elif isinstance(other, MoneyE):
            ex = 1
        return round(ex * other.volume, 1)


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = CentralBank


