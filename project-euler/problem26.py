def period(n):
    rem = [10]
    while True:
        r = 10 * (rem[-1] % n)
        if r == 0: return 0
        if r in rem: return len(rem) - rem.index(r)
        rem.append(r)


mp = md = 0
for d in xrange(1, 1000):
    p = period(d)
    if p > mp:
        mp = p
        md = d

print md