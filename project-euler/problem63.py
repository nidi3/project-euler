m = 0
for s in xrange(1, 30):
    for n in xrange(1, 30):
        if len(str(pow(n, s))) == s: m += 1

print m