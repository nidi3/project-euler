ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = 'hundred'
thousand = 'thousand'


def to_word(n):
    if n >= 1000:
        return to_word(n / 1000) + ' ' + thousand + ('' if n % 1000 == 0 else ' ' + to_word(n % 1000))
    if n >= 100:
        return to_word(n / 100) + ' ' + hundred + ('' if n % 100 == 0 else ' and ' + to_word(n % 100))
    if n >= 20:
        return tens[n / 10 - 2] + ('' if n % 10 == 0 else '-' + to_word(n % 10))
    return ones[n]


s = ''
for n in xrange(1, 1001): s += to_word(n)
print len(s.replace('-', '').replace(' ', ''))