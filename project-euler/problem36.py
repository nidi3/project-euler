from strings import is_palindrom

s = 0
for n in xrange(1, 1000000):
    if is_palindrom(n) and is_palindrom(bin(n)[2:]): s += n

print s