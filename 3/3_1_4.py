class Book:
    def __init__(self, title: str = "", author: str = '', pages: int = 0, year: int = 0):
        self.title = title
        self.author = author
        self. pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', ' author') and type(value) is not str or key in ('pages', ' year') and type(value) is not int:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            super.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев',123, 2022)

