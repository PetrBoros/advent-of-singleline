import re
from collections import Counter
from operator import itemgetter

# Part 1
print sum(map(lambda x: int(x[1]), filter(lambda m: m[2] == ''.join(zip(*sorted(Counter(sorted(list(m[0].replace('-','')))).most_common(), key=lambda e: (-e[1], e[0]))[0:5])[0]), [re.search('([a-z\-]*)-([0-9]*)\[([a-z]*)\]', r).groups() for r in open('input.txt').read().splitlines()])))

# Part 2
print filter(lambda x: 'north' in x[0], map(lambda m: (''.join(chr(((ord(char) - 97 + int(m[1])) % 26) + 97) if char.islower() else char for char in m[0]), m[1]), filter(lambda m: m[2] == ''.join(zip(*sorted(Counter(sorted(list(m[0].replace('-','')))).most_common(), key=lambda element: (-element[1], element[0]))[0:5])[0]), [re.search('([a-z\-]*)-([0-9]*)\[([a-z]*)\]', r).groups() for r in open('input.txt').read().splitlines()])))[0][1]
