class SingletonFive:
    inst_count = 0
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.inst_count <= 4:
            cls.__isinstance = super().__new__(cls)
        cls.inst_count += 1
        return cls.__isinstance

    def __init__(self, name):
        self.name = name



objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять