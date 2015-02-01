def divisable(n):
    for d in xrange(2, 21):
        if n % d != 0: return False
    return True


f = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
n = f
while not divisable(n): n += f

print n