from strings import is_palindrom

max = 0
for x in xrange(2, 1000):
    for y in range(2, 1000):
        v = x * y
        if v > max and is_palindrom(v): max = v

print max