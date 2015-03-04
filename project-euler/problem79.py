from strings import read_split

list = read_split('p079_keylog.txt', '\n')


def possible(l, s):
    a = s.find(l[0])
    if a >= 0:
        b = s.find(l[1], a + 1)
        if b >= 0:
            c = s.find(l[2], b + 1)
            if c >= 0:
                return True
    return False


first = set()
for l in list:
    first.add(l[0])
print first

last = set()
for l in list:
    last.add(l[2])
print last

all = set()
for l in list:
    all.add(l[0])
    all.add(l[1])
    all.add(l[2])
print all


def check(n):
    for first in '123678':
        for last in '012689':
            s = first + str(n) + last
            ok = True
            for l in list:
                if not possible(l, s):
                    ok = False
                    break
            if ok:
                print s
                return True
    return False


n = 1
while not check(n):
    n += 1
