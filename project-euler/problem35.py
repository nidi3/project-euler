import sieve


def rot(n):
    s = str(n)
    return int(s[-1:] + s[:-1])


def rot_prime(s, n):
    for i in xrange(0, len(str(n)) - 1):
        n = rot(n)
        if not sieve.is_prime(s, n): return False
    return True


s = sieve.sieve(1000000)
n = 0
for p in sieve.primes(s):
    if rot_prime(s, p): n += 1

print n
