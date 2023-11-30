# AC, Принята

from math import ceil
n, k = list(map(int, input().split()))
if n == 0:
    print(0)
elif n <= k:
    print(4)
else:
    print(ceil(n * 2 / k) * 2)
