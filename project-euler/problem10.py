import primes

sum = 0
p = primes.primes(primes.sieve(2000100))
i = 0
while p[i] < 2000000:
    sum += p[i]
    i += 1

print sum