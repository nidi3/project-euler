def tri(n):
    while True:
        yield n * (n + 1) / 2
        n += 1


def pent(n):
    while True:
        yield n * (3 * n - 1) / 2
        n += 1


def hex(n):
    while True:
        yield n * (2 * n - 1)
        n += 1


p = h = 0
t = 1
tri = tri(286)
pent = pent(165)
hex = hex(143)
while not t == p == h:
    while t < p or t < h: t = tri.next()
    while p < t or p < h: p = pent.next()
    while h < p or h < p: h = hex.next()

print t