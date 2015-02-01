import factors

s = 0
for i in xrange(2, 10000):
    sf = sum(factors.factors(i)) - i
    if sf != i and sf < 10000 and sum(factors.factors(sf)) - sf == i:
        s += i + sf

print s / 2
