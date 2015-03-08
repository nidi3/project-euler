from primes import is_prime

s = set()
a = 0
while a * a < 50000000:
    a += 1
    while not is_prime(a): a += 1
    ab = b = 0
    while ab < 50000000:
        b += 1
        while not is_prime(b): b += 1
        ab = a * a + b * b * b
        abc = c = 0
        while abc < 50000000:
            c += 1
            while not is_prime(c): c += 1
            abc = ab + c * c * c * c
            if abc < 50000000:
                s.add(abc)

print len(s)