from itertools import *

a = 'fgtnpswd'
b = '84'
c = 'Yana'
d = '1009'
e = 'Xsnx'
c2 = 'yana'
e2 = 'xsnx'


list = [a,b,c,d,e]
list2 = [a, b, c2, d,e2]
k = 0
for i in permutations(list):
    a = ''.join(i)
    if (i[1] == b or i [1] == d) and (i[0] != b or i [1] != d) and not ('841009' in a or '100984' in a):
        k += 1
        print(f'{k}. {a}')

for i in permutations(list2):
    a = ''.join(i)
    if (i[1] == b or i [1] == d) and (i[0] != b or i [1] != d) and not ('841009' in a or '100984' in a):
        k += 1
        print(f'{k}. {a}')