# AC, Принята

def thing(num):
    for i in 'ABC':
        num = num.replace(i, '2')
    for i in 'DEF':
        num = num.replace(i, '3')
    for i in 'GHI':
        num = num.replace(i, '4')
    for i in 'JKL':
        num = num.replace(i, '5')
    for i in 'MNO':
        num = num.replace(i, '6')
    for i in 'PQRS':
        num = num.replace(i, '7')
    for i in 'TUV':
        num = num.replace(i, '8')
    for i in 'WXYZ':
        num = num.replace(i, '9')
    return num

import sys
for line in sys.stdin.readlines():
    print(thing(line.rstrip()))
