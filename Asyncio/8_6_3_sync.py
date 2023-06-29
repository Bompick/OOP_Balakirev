import random
import time


def two(x):
    a = random.randint(1, 10)
    time.sleep(a)
    return print(x, f'  спал {a} сек')


def one(x):
    a = random.randint(1, 10)
    time.sleep(a)
    return print(x, f'  спал {a} сек')


def main():
    one(1)
    two(2)


main()



