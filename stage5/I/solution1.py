# AC, Принята

x, y = map(int, input().split())
n = int(input())

sm = 1e10
xa, ya = x, y
for i in range(n):
    xi, yi = map(int, input().split())
    s = abs(x - xi) + abs(y - yi)
    if s < sm:
        xa, ya = xi, yi
        sm = s

print(xa, ya)

