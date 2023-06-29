class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []
for line in lst_in:
    data = line.split("; ")
    data[-1] = int(data[-1])
    lst_bs.append(BookStudy(*data))


unique_books = len(set([hash(item) for item in lst_bs]))
print(unique_books)