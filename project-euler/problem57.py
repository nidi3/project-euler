def approx(n):
    a = 1
    b = 2
    for x in xrange(1, n):
        a, b = b, a + 2 * b
    return [a + b, b]


s = 0
for n in xrange(1, 1001):
    d = approx(n)
    if len(str(d[0])) > len(str(d[1])):
        s += 1

print s