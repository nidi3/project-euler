from fractions import Fraction

z = float(3) / 7
m = 1
for d in xrange(1, 1000001):
    for n in xrange(int(z * d) - 5, int(z * d) + 1):
        v = float(n) / d
        if v < z and z - v < m and Fraction(n, d) != Fraction(3, 7):
            m = z - v
            dm = d
            nm = n

print Fraction(nm, dm)