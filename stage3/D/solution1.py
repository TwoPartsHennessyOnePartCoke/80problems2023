# AC, Принята

from math import sqrt

R, r, h, b = map(int, input().split())

if R + b > h + r and R > sqrt((h - b + r)**2 + r**2):
    print("YES")
else:
    print("NO")


