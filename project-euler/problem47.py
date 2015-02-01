import factors


def distinct(a, b, c):
    d = 0
    for x in a:
        if not x in b: d += 1
    return d >= c

f1 = factors.prime_factors(1000)
f2 = factors.prime_factors(1001)
f3 = factors.prime_factors(1002)
f4 = factors.prime_factors(1003)
for n in xrange(1004, 1000000):
    if len(f1) >= 4 and len(f2) >= 4 and len(f3) >= 4 and len(f4) >= 4 and \
            distinct(f1, f2, 4) and distinct(f2, f3, 4) and distinct(f3, f4, 4):
        break
    f1, f2, f3, f4 = f2, f3, f4, factors.prime_factors(n)

print n - 4, f1, f2, f3, f4