max = 0


def collatz(n):
    s = 0
    while not n in collatz.values:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        s += 1
    s += collatz.values[n]
    collatz.values[i] = s
    return s


collatz.values = {1: 1}

for i in xrange(2, 1000000):
    s = collatz(i)
    if s > max:
        max = s
        n = i

print n
