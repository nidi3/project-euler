from strings import read_split


def normalize(c):
    if c[0] == 'T':
        return 10, c[1]
    if c[0] == 'J':
        return 11, c[1]
    if c[0] == 'Q':
        return 12, c[1]
    if c[0] == 'K':
        return 13, c[1]
    if c[0] == 'A':
        return 14, c[1]
    return ord(c[0]) - ord('0'), c[1]


def is_suit(c):
    return c[0][1] == c[1][1] == c[2][1] == c[3][1] == c[4][1]


def is_straight(c):
    return c[0][0] + 1 == c[1][0] and c[1][0] + 1 == c[2][0] and c[2][0] + 1 == c[3][0] and c[3][0] + 1 == c[4][0]


def is_4(c):
    return (c[0][0] == c[1][0] and c[1][0] == c[2][0] and c[2][0] == c[3][0]) or \
           (c[1][0] == c[2][0] and c[2][0] == c[3][0] and c[3][0] == c[4][0])


def is_3(c):
    return (c[0][0] == c[1][0] and c[1][0] == c[2][0]) or \
           (c[1][0] == c[2][0] and c[2][0] == c[3][0]) or \
           (c[2][0] == c[3][0] and c[3][0] == c[4][0])


def is_full(c):
    return (c[0][0] == c[1][0] and c[1][0] == c[2][0] and c[3][0] == c[4][0]) or \
           (c[1][0] == c[2][0] and c[2][0] == c[3][0] and c[0][0] == c[4][0]) or \
           (c[2][0] == c[3][0] and c[3][0] == c[4][0] and c[0][0] == c[1][0])


def is_2(c):
    if c[0][0] == c[1][0]: return c[0][0]
    if c[1][0] == c[2][0]: return c[1][0]
    if c[2][0] == c[3][0]: return c[2][0]
    if c[3][0] == c[4][0]: return c[3][0]


def is_2_2(c):
    return (c[0][0] == c[1][0] and c[2][0] == c[3][0]) or \
           (c[0][0] == c[1][0] and c[3][0] == c[4][0]) or \
           (c[1][0] == c[2][0] and c[3][0] == c[4][0])


def eval(s):
    cs = map(lambda c: normalize(c), s.split(' '))
    cs.sort()
    if is_suit(cs) and is_straight(cs):
        v = 10000
    elif is_4(cs):
        v = 9000
    elif is_full(cs):
        v = 8000
    elif is_suit(cs):
        v = 7000
    elif is_straight(cs):
        v = 6000
    elif is_3(cs):
        v = 5000
    elif is_2_2(cs):
        v = 4000
    elif is_2(cs):
        v = 3000 + is_2(cs) * 20 + cs[4][0]
    else:
        v = cs[4][0]
    return v


w = 0
for h in read_split('p054_poker.txt', '\n'):
    a = eval(h[0:14])
    b = eval(h[15:30])
    if a > b: w += 1

print w