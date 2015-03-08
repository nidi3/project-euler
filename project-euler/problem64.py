from math import sqrt, floor


def cont_frac_of_root(q):
    s = set()
    r = sqrt(q)
    a = 1
    b = floor(r)
    l = [b]
    if b != r:
        while (a, b) not in s:
            s.add((a, b))
            a, b = b, (q - b * b) / a
            n = floor((r + a) / b)
            l.append(n)
            a, b = b, n * b - a

    return l


t = 0
for n in xrange(2, 10001):
    if len(cont_frac_of_root(n)) % 2 == 0: t += 1

print t