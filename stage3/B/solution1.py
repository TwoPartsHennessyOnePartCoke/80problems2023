# AC, Принята

n, m, l = map(int, input().split())

s = ['b', 'a', 'ab', 'aba', 'abaab', 'abaababa', 'abaababaabaab', 'abaababaabaababaababa',
     'abaababaabaababaababaabaababaabaab', 'abaababaabaababaababaabaababaabaababaababaabaababaababa',
     'abaababaabaababaababaabaababaabaababaababaabaababaababaabaababaabaababaababaabaababaabaab']

for i in range(11, n):
    s.append(s[i-1] + s[i-2])

ans = s[n - 1]
print(ans[(m - 1):(m - 1 + l)])
