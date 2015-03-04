from strings import to_digit, read_split

names = read_split('p022_names.txt')
names.sort()

s = 0
for i, n in enumerate(names):
    score = reduce(lambda acc, x: acc + to_digit(x, '@'), n[1:-1], 0)
    s += (i + 1) * score

print s
