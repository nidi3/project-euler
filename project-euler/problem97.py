s = 2
for n in xrange(1, 7830457):
    s *= 2
    if s > 100000000000:
        s = int(str(s)[-11:])

print str(28433 * s + 1)[-10:]
