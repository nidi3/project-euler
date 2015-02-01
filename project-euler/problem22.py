from strings import to_digit

f = open('p022_names.txt', 'r')
names = f.read().split(',')
names.sort()

s = 0
for i, n in enumerate(names):
    score = reduce(lambda acc, x: acc + to_digit(x, '@'), n[1:-1], 0)
    s += (i + 1) * score

print s
