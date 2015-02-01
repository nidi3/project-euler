from math import sqrt, floor, fabs


def is_penta(n):
    s = (.5 + sqrt(.25 + 6 * n)) / 3
    return fabs(s - floor(s)) < .00001


def penta(n): return n * (3 * n - 1) / 2


d = 100000000
for n in xrange(1, 2000):
    for m in xrange(1, 2000):
        diff = penta(n + m) - penta(n)
        if is_penta(diff) and is_penta(penta(n + m) + penta(n)) and diff < d:
            d = diff

print d
