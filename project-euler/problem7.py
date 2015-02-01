def num2index(n):
    return (n - 3) / 2


def index2num(i):
    return i * 2 + 3


p = 60000 * [True]
for i in xrange(0, len(p)):
    if p[i]:
        f = index2num(i) * 2
        while num2index(f) < len(p):
            if f % 2 == 1: p[num2index(f)] = False
            f += index2num(i)

n = 2
for i in xrange(0, len(p)):
    if p[i]:
        if n == 10001: print index2num(i)
        n += 1