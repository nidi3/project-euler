import math

from primes import is_prime


def is_prime_and_square(n):
    for s in xrange(0, int(math.floor(math.sqrt(n / 2))) + 1):
        if is_prime(n - 2 * s * s):
            return True
    return False


for n in xrange(3, 10000, 2):
    if not is_prime(n):
        if not is_prime_and_square(n):
            print n
            break
