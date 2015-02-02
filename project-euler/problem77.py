import primes

p = primes.primes(primes.sieve(1000))

r = {}


def sfind(value, v):
    key = value * 1000000 + v
    if key in r: return r[key]
    val = find(value, v)
    r[key] = val
    return val


def find(value, vi):
    m = 0
    e = value / p[vi]
    if e == 0: return m
    for a in xrange(0, e + 1):
        x = p[vi] * a
        if x < value and vi + 1 < len(p): m += sfind(value - x, vi + 1)
        if x == value: m += 1
        if x >= value: break
    return m


for n in xrange(10, 10000):
    if sfind(n, 0) > 5000: break

print n