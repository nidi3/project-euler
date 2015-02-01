d = [False] * 10


def possible(n):
    e = [False] * 10
    while n > 0:
        if d[n % 10] or e[n % 10]: return False
        e[n % 10] = True
        n /= 10
    return True


def put(n, val):
    while n > 0:
        d[n % 10] = val
        n /= 10


def count():
    c = 0
    for i in xrange(0, 10):
        if d[i]: c += 1
    return c


s = set()
d[0] = True
for a in xrange(1, 100):
    if possible(a):
        put(a, True)
        for b in xrange(100, 10000):
            if possible(b):
                put(b, True)
                if possible(a * b) and count() == 6: s.add(a * b)
                put(b, False)
        put(a, False)

print s, sum(s)