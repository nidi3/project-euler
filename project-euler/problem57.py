from maths import cont_fraction


def c(n): return 2


s = 0
for n in xrange(1, 1001):
    d = cont_fraction(n, 1, c)
    if len(str(d[0])) > len(str(d[1])):
        s += 1

print s