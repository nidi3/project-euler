s = set()
for a in xrange(2, 101):
    for b in xrange(2, 101):
        s.add(pow(a, b))

print len(s)