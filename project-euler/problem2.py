s = 0
f1 = 1
f2 = 1
while f1 <= 4000000:
    if f1 % 2 == 0: s += f1
    f1, f2 = f1 + f2, f1

print s