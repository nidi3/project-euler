from fractions import Fraction

a = float(1) / 3
b = float(1) / 2
m = set()
for d in xrange(1, 12001):
    for n in xrange(int(a * d) - 5, int(b * d) + 5):
        v = float(n) / d
        if a < v < b:
            f = Fraction(n, d)
            if f not in m:
                m.add(f)

print len(m)