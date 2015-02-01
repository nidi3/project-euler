d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def pos_to_change():
    i = len(d) - 2
    while d[i] > max(d[i + 1:]): i -= 1
    return i


def exchange_pos(i):
    t = i + 1
    for j in xrange(i + 1, len(d)):
        if d[i] < d[j] < d[t]: t = j
    return t


def fill_rest(f, i):
    f.sort()
    for k in xrange(i, len(d)):
        d[k] = f[k - i]


def exchange(i, t):
    f = d[i + 1:]
    d[i], f[t - i - 1] = f[t - i - 1], d[i]
    return f


def next():
    i = pos_to_change()
    t = exchange_pos(i)
    f = exchange(i, t)
    fill_rest(f, i + 1)


for i in xrange(1, 1000000):
    next()

print reduce(lambda acc, x: acc + chr(x + 48), d, '')
