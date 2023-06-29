from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        for i, j in enumerate(number):
            if i in (4, 9, 14):
                if j != "-":
                    return False
            elif not j.isdigit():
                return False
        return True

    @classmethod
    def check_name(cls, name: str):
        return name.count(' ')==1  and all(map(lambda s: set(s) < set(cls.CHARS_FOR_NAME), name.split(' ')))


print(CardCheck.check_name("SERGEI BALAKIREV"))