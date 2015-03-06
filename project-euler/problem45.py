from polygons import trigonal_gen, pentagonal_gen, hexagonal_gen

p = h = 0
t = 1
tri = trigonal_gen(286)
pent = pentagonal_gen(165)
hex = hexagonal_gen(143)
while not t == p == h:
    while t < p or t < h: t = tri.next()
    while p < t or p < h: p = pent.next()
    while h < p or h < p: h = hex.next()

print t