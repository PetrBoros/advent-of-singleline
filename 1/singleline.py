# Part 1
print (lambda x: abs(x[0])+abs(x[1]))(reduce(lambda s, i: (lambda s, i: [s[0],s[1]+int(i[1:]),s[2]] if s[2] == 0 else ([s[0],s[1]-int(i[1:]),s[2]] if s[2] == 2 else ([s[0]+int(i[1:]),s[1],s[2]] if s[2] == 1 else [s[0]-int(i[1:]),s[1],s[2]])))((lambda s, i: [s[0],s[1],(s[2]-1)%4] if i[0] == 'L' else [s[0],s[1],(s[2]+1)%4])(s, i), i), open('input.txt').read().split(', '), [0,0,0]))
