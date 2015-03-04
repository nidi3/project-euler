import math

min = int(math.sqrt(1020304050607080900))
max = int(math.sqrt(1929394959697989990))
for n in xrange(1010101010, max + 1, 10):
    s = str(n * n)
    if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and \
                    s[14] == '8' and s[16] == '9' and s[18] == '0':
        print n