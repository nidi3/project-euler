from strings import digits_of

n = 1
while not (digits_of(n) == digits_of(2 * n) == digits_of(3 * n) == digits_of(4 * n) == \
                   digits_of(5 * n) == digits_of(6 * n)):
    n += 1

print n