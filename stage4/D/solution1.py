# WA, Тест 1: неверный ответ

import math

n, r = map(int, input().split())
fragments = [list(map(int, input().split())) for i in range(n)]

if fragments[0][0]>fragments[0][1]:
    end=fragments[0][0]
    fragments[0][0]=0
    n+=1
    fragments.append([end,360])

deg_circle = 0
for i in range(n):
    deg_circle += fragments[i][1] - fragments[i][0]

length = (math.pi * r * deg_circle) / 180

for i in range(n):
    if i!=n-1:
        a=fragments[i+1][0]-fragments[i][1]
    else:
        a=360-fragments[i][1]
    if a!=0:
        len=(2*(r/2)*(r/2)-2*(r/2)*(r/2)*math.cos(a))**0.5
    else:
        break
    length+=round(len,2)
print(length)