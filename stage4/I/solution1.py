# TL, Тест 30: превышение лимита времени

m = int(input())
n = int(input())
parts = []

for _ in range(n):
    a, b = map(int, input().split())
    p = [a, b]

    parts = [j for j in parts if (not((p[0] <= j[1]) and (p[1] >= j[0])))]
    parts.append(p)

print(len(parts))
