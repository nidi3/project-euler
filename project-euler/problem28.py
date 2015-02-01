n = 1001
v = 1
p = 2
s = 1
for i in xrange(0, n / 2):
    for j in xrange(0, 4):
        v += p
        s += v
    p += 2

print s