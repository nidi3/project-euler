import pandigits

ps = pandigits.pandigit([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in xrange(0, 1000000):
    d = ps.next()

print pandigits.to_int(d)