from random import randint, choice


class RandomPassword:
    def __init__(self, psw_chars="qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", min_length=5, max_length=20):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join([choice(self.__psw_chars) for i in
                        range(randint(self.__min_length, self.__max_length))])


rnd = RandomPassword()
psw = rnd()

lst_pass = [psw for i in range(3)]
print(lst_pass)


