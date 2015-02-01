def __num2index(n):
    return (n - 3) / 2


def __index2num(i):
    return i * 2 + 3


def sieve(max):
    p = __num2index(max) * [True]
    for i in xrange(0, len(p)):
        if p[i]:
            f = __index2num(i) * 2
            while __num2index(f) < len(p):
                if f % 2 == 1: p[__num2index(f)] = False
                f += __index2num(i)
    return p


def primes(s):
    r = [2]
    for i in xrange(0, len(s)):
        if s[i]: r.append(__index2num(i))

    return r


def is_prime(s, n): return n % 2 == 1 and s[__num2index(n)]
