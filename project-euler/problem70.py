from math import sqrt

from strings import to_digit

from factors import prime_factors

from primes import sieve, is_sieve_prime


def totient(n):
    ps = prime_factors(n)
    t = n
    for p in ps:
        t *= (1 - float(1) / p)
    return int(t)


def digits(n):
    d = [0] * 10
    s = str(n)
    for c in s:
        d[to_digit(c)] += 1
    return d


s = sieve(100000)
z = 2
min = int(.5 * sqrt(10000000))
max = int(1.5 * sqrt(10000000))
for n in xrange(min, max):
    if is_sieve_prime(s, n):
        for m in xrange(n + 1, max):
            if n * m < 10000000 and is_sieve_prime(s, m):
                t = totient(n * m)
                x = float(n * m) / t
                if x < z and digits(n * m) == digits(t):
                    p = n * m
                    z = x

print p