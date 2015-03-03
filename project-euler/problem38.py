from pandigits import is_pandigit

m = 0
for n in xrange(10000):
    s = 0
    d = ''
    while len(d) < 10:
        s += 1
        d += str(n * s)
        dv = int(d)
        if is_pandigit(dv):
            if dv > m: m = dv

print m