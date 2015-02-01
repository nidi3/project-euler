def coord2Index(x, y): return x * 100 + y


def set(x, y, c): s[coord2Index(x, y)] = c


def get(x, y): return s[coord2Index(x, y)]


s = {}
set(1, 0, 1)
set(0, 1, 1)
set(1, 1, 2)

for d in xrange(2, 21):
    set(0, d, get(0, d - 1))
    set(d, 0, get(d - 1, 0))
    for n in xrange(1, d):
        set(n, d, get(n, d - 1) + get(n - 1, d))
        set(d, n, get(d - 1, n) + get(d, n - 1))
    set(d, d, get(d - 1, d) + get(d, d - 1))

print get(20,20)