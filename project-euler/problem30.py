from strings import to_digit

ss = 0
for n in xrange(10, 6 * pow(9, 5)):
    s = 0
    for c in str(n):
        s += pow(to_digit(c), 5)
    if s == n: ss += s

print ss
