# WA, Тест 7: неверный ответ

N, M, m = map(int, input().split())

if N < 4 and M < 4:
    ans = (N + M) * 2
else:
    ans = 12 + 4 * (N - 3 + M - 3)
print(ans % m)
