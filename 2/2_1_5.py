class Money:
    @classmethod
    def __check_money(cls, money: int):
        return True if type(money) == int and money>=0 else False

    def __init__(self, money):
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money: int):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money

