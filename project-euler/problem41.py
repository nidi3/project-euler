import primes
import pandigits


for r in xrange(2, 11):
    for pd in pandigits.pandigit([x for x in xrange(1, r)]):
        p = pandigits.to_int(pd)
        if primes.is_prime(p): m = p

print m