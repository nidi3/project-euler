from strings import to_digit

mem = {}


def eighty_nine(m):
    n = m
    while n != 1 and n != 89 and n not in mem:
        n = reduce(lambda accu, v: accu + to_digit(v) * to_digit(v), str(n), 0)
    if m < 1000:
        if n in mem:
            mem[m] = mem[n]
        else:
            mem[m] = n == 89
        return mem[m]
    else:
        return mem[n]

s = 0
for n in xrange(1, 10000000):
    if eighty_nine(n): s += 1

print s