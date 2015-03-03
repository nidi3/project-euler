from primes import is_prime

p = 0
n = 1
while p == 0 or 10 * p >= (2 * n - 1):
    if is_prime(n * n + n + 1): p += 1
    if is_prime(n * n + 2 * n + 2): p += 1
    if is_prime(n * n + 3 * n + 3): p += 1
    n += 2

print n