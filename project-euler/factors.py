from math import sqrt, floor, ceil


def prime_factors(n):
    def possible(n):
        yield 2
        s = int(floor(sqrt(n)))
        for i in xrange(3, s, 2): yield i

    fs = []
    for i in possible(n):
        if n % i == 0:
            fs.append(i)
            while n % i == 0: n /= i
    if n != 1: fs.append(n)
    return fs


def factors(n):
    fs = []
    s = int(ceil(sqrt(n)))
    if s == sqrt(n): fs.append(s)
    for i in xrange(1, s):
        if n % i == 0:
            fs.append(i)
            fs.append(n / i)

    return fs