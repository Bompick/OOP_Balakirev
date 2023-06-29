class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('call')
        self.__counter += step
        return self.__counter


c = Counter()
c()
c(18)
res = c(101)
print(res)
