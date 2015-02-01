import primes

s = primes.sieve(1000000)
p = primes.primes(s)
hl = hm = 0
for a in xrange(0, len(p)):
    m = 0
    b = a
    while b < len(p) and m < 1000000:
        if b - a > hl and primes.is_sieve_prime(s, m):
            hl = b - a
            hm = m
        m += p[b]
        b += 1

print hm