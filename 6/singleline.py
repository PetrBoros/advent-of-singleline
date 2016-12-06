from collections import Counter

print map(''.join,zip(*[(c[0][0],c[-1][0]) for c in map(lambda x:Counter(x).most_common(),zip(*open('input.txt').read().splitlines()))]))