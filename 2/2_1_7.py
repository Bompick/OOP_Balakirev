class Book:

    @classmethod
    def __to_check_str(cls, a):
        if type(a) == str:
            return True
        else:
            raise ValueError ("Yt nf ")

    @classmethod
    def __to_check_int(cls, a):
        if type(a) == int:
            return True
        else:
            raise ValueError ("Yt nf ")

    def __init__(self, author, title, price):
        if self.__to_check_str(author) and self.__to_check_str(title) and self.__to_check_int(price):
            self.__author = author
            self.__title = title
            self.__price = price

    def set_title(self, title):
        if self.__to_check_str(title):
            self.__title = title

    def set_author(self, author):
        if self.__to_check_str(author):
            self.__author = author

    def set_price(self, price):
        if self.__to_check_int(price):
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price
