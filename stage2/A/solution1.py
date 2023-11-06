# AC, Принята

x, y, a, b = map(int, input().split())
if (x == a) and (y == b):
    print('0')
elif (abs(x - a) == abs(y - b)) or (x == a) or (y == b):
    print('1')
else:
    print('2')
