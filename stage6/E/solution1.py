# AC, Принята

n = int(input())

up = n ** 2
bottom = (n - 2) ** 2 if n >= 3 else 0

print(up + bottom + 1)
