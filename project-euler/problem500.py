from primes import sieve, is_sieve_prime

s = sieve(8000000)


def max_factors(end):
    p = 1
    f = 0

    m = 2
    while m < end:
        p *= m
        m *= m
        f += 1
    for n in xrange(3, end, 2):
        if is_sieve_prime(s, n):
            m = n
            while m < end:
                p *= m
                m *= m
                f += 1

    print p % 500500507


max_factors(7370050)