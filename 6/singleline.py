from collections import Counter

# Part 1
print(next(map(''.join,zip(*[c[0][0] for c in map(lambda x:Counter(x).most_common(),zip(*open('input.txt').read().splitlines()))]))))

# Part 2
print(next(map(''.join,zip(*[c[-1][0] for c in map(lambda x:Counter(x).most_common(),zip(*open('input.txt').read().splitlines()))]))))