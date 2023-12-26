# AC, Принята

alf = 'abcdefghijklmnopqrstuvwxyz'

for j in range(2):
    s = input().lower()

    for i in range(len(s)):
        if s[i] not in alf:
            s = s.replace(s[i], ' ', 1)

    s = set(s.split())

    if j == 0:
        s1 = s
    else:
        ans = s1.intersection(s)
        print(*sorted(list(ans)))
