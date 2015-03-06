def max(a, b): return a if a > b else b


def array(x, y): return [[0 for i in xrange(x)] for i in xrange(y)]


from math import sqrt
from fractions import gcd


def pythagorean_triple(max):
    for x in xrange(1, int(sqrt(max))):
        for y in xrange(1, x):
            if gcd(x, y) == 1 and (x - y) % 2 == 1:
                a = x * x - y * y
                b = 2 * x * y
                c = x * x + y * y
                k = 1
                while k * (a + b + c) <= max:
                    yield k * a, k * b, k * c
                    k += 1


def factorial(n):
    f = 1
    for i in xrange(2, n + 1): f *= i
    return f


def cont_fraction(n, start, coeff):
    a = 1
    b = coeff(n-1)
    for x in xrange(n - 2, -1, -1):
        a, b = b, a + coeff(x) * b
    return [a + start * b, b]

def choose(n, m):
    if n == 0:
        return []
    if n == 1:
        return [[x] for x in xrange(0, m)]
    if n == m:
        return [[x for x in xrange(0, m)]]
    c = choose(n - 1, m - 1)
    a = [[m - 1] + x for x in c]
    b = choose(n, m - 1)
    return a + b

def to_list(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n /= 10
    l.reverse()
    return l


def to_num(l):
    v = 0
    for e in l:
        v = 10 * v + e
    return v