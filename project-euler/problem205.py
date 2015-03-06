def sum_count(max, depth):
    p = [0] * (1 + max * depth)
    vs = [0] * (depth + 1)

    def do_fill(depth):
        if depth == 0:
            p[sum(vs)] += 1
        else:
            for i in xrange(1, max + 1):
                vs[depth] = i
                do_fill(depth - 1)

    do_fill(depth)
    return p


def p_bigger(sc, n):
    s = 0
    for i in xrange(n + 1, len(sc)):
        s += sc[i]
    return float(s) / sum(sc)


sc_pete = sum_count(4, 9)
sc_colin = sum_count(6, 6)

p = 0
for i in xrange(0, len(sc_colin)):
    p += float(sc_colin[i]) / sum(sc_colin) * p_bigger(sc_pete, i)

print round(p,7)