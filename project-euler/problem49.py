from primes import sieve, is_sieve_prime
from strings import digits_of


def find():
    p = sieve(10000)
    for n in xrange(1488, 10000):
        for s in xrange(1, (10000 - n) / 2):
            d1 = digits_of(n)
            d2 = digits_of(n + s)
            d3 = digits_of(n + 2 * s)
            if d1 == d2 and d2 == d3 and \
                    is_sieve_prime(p, n) and is_sieve_prime(p, n + s) and is_sieve_prime(p, n + 2 * s):
                print str(n) + str(n + s) + str(n + 2 * s)
                return


find()