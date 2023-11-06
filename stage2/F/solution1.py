# TL, Тест 12: превышение лимита времени

from math import floor, ceil, sqrt
n = int(input())

a1 = 1
top = floor(n / 2)
while True:
    c = a1 - a1**2
    an_approx = floor(sqrt(2*n-c))
    for i in range(an_approx, an_approx+ceil(sqrt(an_approx))+1):
        if 2*n == i**2+i+c:
            print(i - a1 + 1)
            exit()
    a1 += 1
