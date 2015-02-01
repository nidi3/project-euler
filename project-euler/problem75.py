from math import sqrt
from fractions import gcd

m = 1500000
ls = [0] * (m + 1)
for x in xrange(1, int(sqrt(m))):
    for y in xrange(1, x):
        if gcd(x, y) == 1 and (x - y) % 2 == 1:
            a = x * x - y * y
            b = 2 * x * y
            c = x * x + y * y
            k = 1
            while k * (a + b + c) <= m:
                ls[k * (a + b + c)] += 1
                k += 1

s = 0
for i in xrange(1, m + 1):
    if ls[i] == 1: s += 1

print s