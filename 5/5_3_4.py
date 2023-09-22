def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except ValueError:
        raise TypeError('все числа должны быть целыми')


while True:
    try:
        data_output = input_int_numbers()
    except TypeError:
        continue
    else:
        print(' '.join((map(str, data_output))))
        break


