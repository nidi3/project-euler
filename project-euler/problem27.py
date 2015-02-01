from sieve import sieve, is_prime

s = sieve(100000)

m = 0
c = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        n = 0
        while is_prime(s, n * n + a * n + b): n += 1
        if n > m:
            m = n
            c = a * b

print c