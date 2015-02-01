import sieve

sum = 0
p = sieve.sieve(1100000)
i = 0
while p[i] < 2000000:
    sum += p[i]
    i += 1

print sum