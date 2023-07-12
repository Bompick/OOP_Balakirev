
def logger(func, func_name, lst_to_add):
    def wrapper(*args, **kwargs):
        lst_to_add.append(func_name)
        res = func(*args, **kwargs)
        return res
    return wrapper


def class_log(lst):
    def func_decorator(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, logger(v, k, lst))
        return cls
    return func_decorator


vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

a = Vector(1,2,3)
print(vector_log)
