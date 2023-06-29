class FileAcceptor:
    def __init__(self, *args):
        self.lst = [*args]

    def __call__(self, filename):
        return self == filename

    def __eq__(self, other):
        ras = other[other.rfind('.')+1:]
        return ras in self.lst

    def __add__(self, other):
        if not isinstance(other, FileAcceptor):
            raise TypeError("Type!!!!!")
        r1 = set(self.lst)
        r2 = set(other.lst)
        fin = r1 | r2
        return FileAcceptor(*fin)

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc",
             "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)
