class PrimaryKeyError(Exception):
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'
        else:
            if 'id' or 'pk' in kwargs:
                self.message = f'Значение первичного ключа {list(kwargs.keys())[0]} = {kwargs[list(kwargs.keys())[0]]} недопустимо'

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as p:
    print(p)
