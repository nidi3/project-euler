def sieve(size):
    def num2index(n):
        return (n - 3) / 2

    def index2num(i):
        return i * 2 + 3

    p = size * [True]
    for i in xrange(0, size):
        if p[i]:
            f = index2num(i) * 2
            while num2index(f) < size:
                if f % 2 == 1: p[num2index(f)] = False
                f += index2num(i)

    r = [2]
    for i in xrange(0, size):
        if p[i]: r.append(index2num(i))

    return r
