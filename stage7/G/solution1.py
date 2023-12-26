# TL, Тест 5: превышение лимита времени

from math import sqrt

n = int(input())
m = list()
c = 0

for i in range(n):
    x, y = map(int, input().split())
    for j in m:
        if (x == j[0] and abs(y - j[1]) == 2018) or (y == j[1] and abs(x - j[0]) == 2018):
            c += 1
        elif abs(x - j[0]) > 2018 or abs(y - j[1]) > 2018:
            continue
        elif abs(x - j[0]) == 2018 and abs(y - j[1]) == 2018:
            continue
        else:
            dist = sqrt(abs(x - j[0])**2 + abs(y - j[1])**2)
            if dist == 2018:
                c += 1

    m.append([x, y])

print(c)
