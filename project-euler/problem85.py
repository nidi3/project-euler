def rect(w, h):
    r = 0
    for x in xrange(1, w + 1):
        for y in xrange(1, h + 1):
            r += (w - x + 1) * (h - y + 1)

    return r


m = 2000000
d = m
for w in xrange(1, 2100):
    if rect(w, w) > m: break
    for h in xrange(w, 2100):
        v = m - rect(w, h)
        diff = v if v > 0 else -v
        if diff < d:
            d = diff
            a = w * h
        if v < 0:
            break

print a