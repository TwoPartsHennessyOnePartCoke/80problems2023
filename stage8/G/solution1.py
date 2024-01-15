# AC, Принята

n = int(input())
result, m = 1, 1
while n >= ((1 + m) * m // 2):
    if (n - (1 + m) * m // 2) % m == 0:
        result = m
    m += 1
print(result)
