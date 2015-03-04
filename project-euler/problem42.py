from strings import to_digit,read_split

tri = []
for n in xrange(0, 20):
    tri.append(n * (n + 1) / 2)

words = read_split('p042_words.txt')

tw = 0
for word in words:
    s = 0
    for w in word[1:-1]:
        s += to_digit(w, '@')
    for t in tri:
        if s == t: tw += 1

print tw