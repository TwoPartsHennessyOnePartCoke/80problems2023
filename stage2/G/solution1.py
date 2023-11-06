# AC, Принята

def dl(a):
    d = [1]
    b = 2
    while b*b <= a:
        if a % b == 0:
            d.append(b)
            d.append(a // b)
        b += 1
    d.append(a)
    return sorted(d)


n = int(input())

sm = 1e13
d = dl(n)
for i in d:
    d1 = dl(n / i)
    for j in d1:
        d2 = dl(n / (i * j))
        for k in d2:
            if i*j*k == n:
                s = 2*i*j + 2*j*k + 2*k*i
                if s < sm:
                    sm = s

print(int(sm))