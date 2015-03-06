from polygons import is_pentagonal, pentagonal

d = 100000000
for n in xrange(1, 2000):
    for m in xrange(1, 2000):
        diff = pentagonal(n + m) - pentagonal(n)
        if is_pentagonal(diff) and is_pentagonal(pentagonal(n + m) + pentagonal(n)) and diff < d:
            d = diff

print d
