import re
from operator import or_, add
from itertools import chain
from functools import reduce

# Part 1
print(sum([1 if x == (True, False) else 0 for x in map(lambda x: (reduce(or_, x[0::2]),reduce(or_, x[1::2])), map(lambda r: [reduce(or_, [x[a] == x[a+3] and x[a+1] == x[a+2] and x[a] != x[a+1] for a in range(len(x)-3)]) for x in r], [filter(None, re.findall('([a-z]*)', row)) for row in open('input.txt').read().splitlines()]))]))

# Part 2
print(sum([1 if len(x-y) < len(x) else 0 for (x,y) in map(lambda x: (set(reduce(add, [a for a in x[0::2]])), set(map(lambda t: t[1]+t[0]+t[1], filter(lambda o: o[0] != o[1], reduce(add, [a for a in x[1::2]]))))), [list(map(lambda x: list(chain([a for (a,b) in re.findall(r'(?=((.).\2))', x)])), filter(None, re.findall('([a-z]*)', row)))) for row in open('input.txt').read().splitlines()])]))
