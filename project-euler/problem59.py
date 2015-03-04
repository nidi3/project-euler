from strings import read_split

cypher = ''
for c in read_split('p059_cipher.txt'):
    cypher += chr(int(c))

for a in xrange(97, 122):
    for b in xrange(97, 122):
        for c in xrange(97, 122):
            s = ''
            for d in xrange(0, len(cypher) - 1, 3):
                s += chr(ord(cypher[d]) ^ a) + chr(ord(cypher[d + 1]) ^ b) + chr(ord(cypher[d + 2]) ^ c)
            s += chr(ord(cypher[len(cypher)-1]) ^ a)
            if s.find('the') >= 0 and s.find('to') >= 0 and s.find('of') >= 0 and s.find('and') >= 0 and \
                            s.count(' ') > 20:
                print s
                print reduce(lambda accu, v: accu + ord(v), s, 0)
