from maths import pythagorean_triple

m = 1000
ls = [0] * (m + 1)
pts = pythagorean_triple(m)
for pt in pts:
    ls[pt[0] + pt[1] + pt[2]] += 1

v = 0
s = 0
for i, l in enumerate(ls):
    if l > v:
        v = l
        s = i

print s