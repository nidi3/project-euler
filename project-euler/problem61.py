from polygons import is_trigonal, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal

s = set()
l = []


def check(n):
    def rec(c):
        a = 100 * (n % 100)
        if a >= 1000:
            s.add(c)
            l.append(n)
            if len(s) == 6 and l[0] / 100 == l[5] % 100:
                print sum(l)
            else:
                for m in xrange(a, a + 100): check(m)
            s.remove(c)
            l.pop(len(l) - 1)

    if 't' not in s and is_trigonal(n): rec('t')
    if 's' not in s and is_square(n): rec('s')
    if 'p' not in s and is_pentagonal(n): rec('p')
    if 'h' not in s and is_hexagonal(n): rec('h')
    if 'e' not in s and is_heptagonal(n): rec('e')
    if 'o' not in s and is_octagonal(n): rec('o')


for n in xrange(1000, 10000):
    check(n)

