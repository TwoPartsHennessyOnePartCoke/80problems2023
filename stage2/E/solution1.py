# AC, Принята

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
br = b[::-1]

c1 = []
c2 = []

for i in range(n):
    c1.append(a[i] + b[i])
    c2.append(a[i] + br[i])

print(max(min(c1), min(c2)))
