max = 100

r = {}


def sfind(value, v):
    key = value * 1000 + v
    if key in r: return r[key]
    val = find(value, v)
    r[key] = val
    return val


def find(value, v):
    m = 0
    for a in xrange(0, max + 1):
        x = v * a
        if x < value and v < max: m += sfind(value - x, v + 1)
        if x == value: m += 1
        if x >= value: break
    return m


print sfind(max, 1) - 1