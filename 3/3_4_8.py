class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) is Book:
            self.book_list.remove(other)
        elif type(other) is int:
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


book = Book('title', 'author', 2023)
lib = Lib()
lib = lib + book
book2 = Book('2', 'RB', 2022)
lib = lib + book2
lib = lib - book