def palindrom(n):
    s = str(n)
    for i in xrange(len(s) / 2):
        if s[i] != s[len(s) - i - 1]: return False
    return True


max = 0
for x in xrange(2, 1000):
    for y in range(2, 1000):
        v = x * y
        if v > max and palindrom(v): max = v

print max