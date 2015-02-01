from math import sqrt, ceil


def possible(n):
    yield 2
    s = int(ceil(sqrt(n)))
    for i in xrange(3, s, 2): yield i


def factors(n):
    fs = []
    for i in possible(n):
        if n % i == 0:
            while n % i == 0: n /= i
            fs.append(i)
    if n != 1: fs.append(n)
    return fs


print max(factors(600851475143))