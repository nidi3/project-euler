vs = [1, 2, 5, 10, 20, 50, 100, 200]


def find(value, vi):
    m = 0
    for a in xrange(0, 201):
        x = vs[vi] * a
        if x < value and vi + 1 < len(vs): m += find(value - x, vi + 1)
        if x == value: m += 1
        if x > value: break
    return m


print find(200, 0)