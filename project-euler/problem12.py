import factors

n = 1
i = 2
while len(factors.factors(n)) <= 500:
    n += i
    i += 1

print n