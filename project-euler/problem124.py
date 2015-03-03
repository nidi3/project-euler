from factors import prime_factors

s = []
for n in xrange(1, 100001):
    s.append((n, reduce(lambda accu, v: accu * v, prime_factors(n), 1)))

s.sort(key=lambda e: e[0] + 1000000 * e[1])
print s[10000 - 1][0]