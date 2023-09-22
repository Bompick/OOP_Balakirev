class DefenedVeector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return True


v1 = [1, 2, 3]
v2 = [10, 11]

try:
    with DefenedVeector(v1) as dv:
        for i, item in enumerate(dv):
            dv[i] += v2[i]
except Exception:
    print('Ошибка')


print(v1)
