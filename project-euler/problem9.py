from math import sqrt

for a in xrange(1, 1000):
    for b in xrange(a, 1000):
        c = sqrt(a * a + b * b)
        if a + b + c == 1000: print int(a * b * c)