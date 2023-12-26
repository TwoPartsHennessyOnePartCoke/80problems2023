# TL, Тест 10: превышение лимита времени

s = input()
n = int(input())
m = [0 for k in range(len(s))]

for i in range(n):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        m[j] += 1

ans = ''
for i in range(len(m)):
    if m[i] % 2 != 0:
        ans += '(' if s[i] == ')' else ')'
    else:
        ans += '(' if s[i] == '(' else ')'

print(ans)
