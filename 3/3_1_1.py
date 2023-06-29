class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        print("ROBERT - 1")
        if item == 'y':
            raise ValueError("К этому атрибуту обращаться нельзя")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("Elmira")
        if key == 'z':
            raise ValueError("Недопутимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('Такой атрибут не существует')
        return False # Вывод  сообщения и возврат False вместо ошибки

    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)

p = Point(1, 2)
del p.x
print(p.__dict__)
# print(p.yy)
# p.y = 3
#a = p.y

