# AC, Принята

n = int(input())

def calc(r, x, y):
    p1 = r / (r - y)
    return x * p1 / (p1 + 1)

for _ in range(n):
    r, x, y = map(int, input().split())
    print(round(calc(r, x, y), 2))
