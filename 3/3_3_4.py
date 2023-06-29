class Model:
    def __init__(self):
        self.data = "Model"

    def query(self, **kwargs):
        self.data = kwargs

    def __str__(self):
        b = str(self.__class__)
        e = b.rfind("'")
        if self.data != "Model":
            dic = [f'{i[0]} = {i[-1]}' for i in self.data.items()]
            return f"{b[b.rfind('.') + 1:e]}:{','.join(dic)}"
        else:
            return self.data




model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)






