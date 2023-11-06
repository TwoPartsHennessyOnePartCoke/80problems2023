# AC, Принята

from math import sqrt, asin

def area(r, h):
    return 2*r**2*asin(sqrt(h/(2*r)))+(h-r)*sqrt(h*(2*r-h))

d, l, n = map(int, input().split())
r = d / 2
for _ in range(n):
    v = int(input())
    r_area = v / (1000 * l)
    # binary search with precision 1e-7
    low = 0
    high = d
    while high - low > 1e-7:
        mid = (low + high) / 2
        if area(r, mid) < r_area:
            low = mid
        else:
            high = mid
    print('{:.7f}'.format(high))
