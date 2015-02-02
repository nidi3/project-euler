from maths import factorial
from strings import to_digit

cs = {1: 1, 2: 1, 169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2, 145: 1, 40585: 1}


def facsum(n):
    return reduce(lambda acc, v: acc + factorial(to_digit(v)), str(n), 0)


def chain(n):
    s = 0
    m = n
    while m not in cs:
        m = facsum(m)
        s += 1
    cs[n] = s + cs[m]
    return cs[n]


m = 0
for n in xrange(1, 1000000):
    if chain(n) == 60: m += 1

print m