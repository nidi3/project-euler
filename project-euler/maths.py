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
