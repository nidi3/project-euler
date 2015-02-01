import factors

abundants = []
sums = [False] * 28123
for n in xrange(1, 28123):
    if sum(factors.factors(n)) - n > n: abundants.append(n)

for i in xrange(0, len(abundants)):
    for j in xrange(i, len(abundants)):
        a = abundants[i]
        b = abundants[j]
        if a + b >= len(sums): break
        sums[a + b] = True

s = 0
for i, sum in enumerate(sums):
    if not sum: s += i

print s