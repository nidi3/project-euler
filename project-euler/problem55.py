from strings import is_palindrom

def is_lychrel(n):
    n += int(str(n)[::-1])
    i = 0
    while i < 50 and not is_palindrom(n):
        n += int(str(n)[::-1])
        i += 1
    return i == 50


s = 0
for n in xrange(0, 10000):
    if is_lychrel(n): s += 1

print s