# WA, Тест 11: неверный ответ

def d(n,c):
    l=list(range(1,n+1))
    r=0
    for i in range(n):
        t=c[i]
        for j in range(n):
            if j!=i:
                t*=(n+1-l[j])/(l[i]-l[j])
        r+=t
    return r

N=int(input())
coins=[int(i) for i in input().split()]

polynom=d(N,coins)

print(round(polynom))
