import math

from maths import to_list, to_num


def hash(n):
    h = [0] * 11
    h[0] = 1
    for d in to_list(n):
        h[d + 1] += 1
    return to_num(h)


def find(z, num):
    res = []
    m = {}
    min = 10 ** z
    max = 10 ** (z + 1)
    for n in xrange(int(math.pow(min, float(1) / 3)), int(math.pow(max, float(1) / 3))):
        h = hash(n * n * n)
        if h in m:
            l = m[h]
            l.append(n)
            if len(l) == num:
                res.append(l)
        else:
            m[h] = [n]

    return res


for n in xrange(7, 12):
    f = find(n, 5)
    if len(f) > 0:
        print f[0][0]**3
        break