from strings import to_digit

s = ''
i = 1
while len(s) < 1000000:
    s += str(i)
    i += 1

print to_digit(s[0]) * to_digit(s[9]) * to_digit(s[99]) * to_digit(s[999]) * to_digit(s[9999]) * \
      to_digit(s[99999]) * to_digit(s[999999])