import primes


def left_prime(n):
    st = str(n)
    for i in xrange(0, len(st)):
        if not primes.is_prime(int(st[i:])): return False
    return True


def right_prime(n):
    st = str(n)
    for i in xrange(1, len(st)):
        if not primes.is_prime(int(st[:-i])): return False
    return True


n = 13
i = 4
s = 0
c = 0
while c < 11:
    if left_prime(n) and right_prime(n):
        s += n
        c += 1

    n += i
    i = 10 - i

print s