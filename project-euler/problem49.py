from primes import sieve, is_sieve_prime
from strings import to_digit


def digits(n):
    d = [0] * 10
    s = str(n)
    for c in s:
        d[to_digit(c)] += 1
    return d

def find():
    p = sieve(10000)
    for n in xrange(1488, 10000):
        for s in xrange(1, (10000 - n) / 2):
            d1 = digits(n)
            d2 = digits(n + s)
            d3 = digits(n + 2 * s)
            if d1 == d2 and d2 == d3 and \
                    is_sieve_prime(p, n) and is_sieve_prime(p, n + s) and is_sieve_prime(p, n + 2 * s):
                print str(n) + str(n + s) + str(n + 2 * s)
                return

find()