# AC, Принята

n = int(input())

a, b = map(int, input().split())
s = [[a, b]]
for i in range(n - 1):
    a, b = map(int, input().split())
    for j in range(len(s)):
        if (a <= s[j][1]) and (b >= s[j][0]):
            s[j][0] = min(a, s[j][0])
            s[j][1] = max(b, s[j][1])

            clr = 0
            while clr != 1:
                a, b = s[j][0], s[j][1]
                for k in range(len(s)):
                    if (k != j) and (a <= s[k][1]) and (b >= s[k][0]):
                        s[k][0] = min(a, s[k][0])
                        s[k][1] = max(b, s[k][1])
                        s.pop(j)
                        j = k if k < j else (k - 1)
                        break
                else:
                    clr = 1
            break
    else:
        s.append([a, b])

ans = 0
for i in s:
    ans += (i[1] - i[0])

print(ans)
