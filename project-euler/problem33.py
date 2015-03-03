from fractions import Fraction

f = 1
for a in xrange(10, 100):
    for b in xrange(a + 1, 100):
        am = a % 10
        bm = b % 10
        ad = a / 10
        bd = b / 10
        if bm != 0 and am == bd and float(a) / b == float(ad) / bm:
            f *= Fraction(a, b)

print f