from strings import is_palindrom

n = set()
t = 0
for a in xrange(1, 10000):
    b = a
    s = b * b
    while True:
        b += 1
        s += b * b
        if s >= 1e8: break
        if is_palindrom(s): n.add(s)

print sum(n)