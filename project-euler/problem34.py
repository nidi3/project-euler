from strings import to_digit


def fac(n):
    s = 1
    while (n > 1):
        s *= n
        n -= 1
    return s


m = 0
for n in xrange(3, 7 * fac(9)):
    s = 0
    for c in str(n): s += fac(to_digit(c))
    if s == n: m += s

print m
