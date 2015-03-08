from primes import sieve, is_sieve_prime, is_prime

s = sieve(10000000)
ns = [0] * 5


def prime(n):
    return is_sieve_prime(s, n) if n < 10000000 else is_prime(n)


def check(i, sn):
    for j in xrange(0, i):
        if not prime(int(ns[j] + sn)) or not prime(int(sn + ns[j])):
            return False
    return True


def find(i):
    a = 3 if i == 0 else int(ns[i - 1]) + 2
    for n in xrange(a, 8500):
        if prime(n):
            sn = str(n)
            if check(i, sn):
                ns[i] = sn
                if i < 4:
                    find(i + 1)
                else:
                    t = reduce(lambda accu, v: accu + int(v), ns, 0)
                    print t
