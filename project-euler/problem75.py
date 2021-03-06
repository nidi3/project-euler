from maths import pythagorean_triple

m = 1500000
ls = [0] * (m + 1)
pts = pythagorean_triple(m)
for pt in pts:
    ls[pt[0] + pt[1] + pt[2]] += 1

s = 0
for i in xrange(1, m + 1):
    if ls[i] == 1: s += 1

print s