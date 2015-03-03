def is_inc(n):
    s = str(n)
    for x in xrange(1, len(s)):
        if s[x - 1] > s[x]: return False
    return True


def is_dec(n):
    s = str(n)
    for x in xrange(1, len(s)):
        if s[x - 1] < s[x]: return False
    return True


def is_bouncy(n): return not is_inc(n) and not is_dec(n)


b = 0
nb = 99
for n in xrange(100, 10000001):
    if is_bouncy(n):
        b += 1
    else:
        nb += 1

    if b == 99 * nb:
        print n
        break