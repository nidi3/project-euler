from strings import read_split

d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
c = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'),
     (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]


def format(n):
    s = ''
    i = len(c) - 1
    while n > 0:
        while c[i][0] <= n:
            s += c[i][1]
            n -= c[i][0]
        i -= 1
    return s


def parse(s):
    v = 0
    for i in xrange(0, len(s) - 1):
        c = d[s[i]]
        if d[s[i + 1]] > c:
            v -= c
        else:
            v += c
    return v + d[s[-1:]]


nums = read_split('p089_roman.txt', '\n')
s = 0
for num in nums:
    s += len(num) - len(format(parse(num)))

print s