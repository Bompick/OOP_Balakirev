matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
step = (2, 2)
size = (2, 2)


def find_max(table, size, step):
    new = []
    fin = []
    z = 0
    q = 0
    flag = True
    while flag is True:
        s = []
        for i in range(0+z*step[1], size[0]+z*step[1]):
            for j in range(0+q*step[0], size[1]+q*step[0]):
                try:
                    s.append(table[i][j])
                except IndexError:
                    break
        if len(s) == size[0]*size[1]:
            new.append(max(s))
            q += 1
        else:
            if len(new) != 0:
                fin.append(new)
                z += 1
                j = q = 0
                s = new = []
            else:
                flag = False
                return fin


print(find_max(matrix, size, step))
