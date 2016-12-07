from itertools import chain

# Part 1
print(sum(map(lambda t: 1 if t[0]+t[1] > t[2] else 0, [tuple(sorted(map(int, x.split()))) for x in open('input.txt').read().splitlines()])))

# Part 2
print(sum(map(lambda t: 1 if t[0]+t[1] > t[2] else 0, (lambda x: [tuple(sorted(x[i:i+3])) for i in range(0,len(x)-2,3)])(list(chain(*map(list, zip(*[map(int, x.split()) for x in open('input.txt').read().splitlines()]))))))))
