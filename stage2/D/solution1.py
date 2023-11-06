# TL, Тест 7: превышение лимита времени

def dl(a):
    if a == 1:
        return 1

    d = [1]
    b = 2
    while b*b <= a:
        if a % b == 0:
            d.append(b)
            if b != (a // b):
                d.append(a // b)
        b += 1
    d.append(a)
    return len(d)


n = int(input())

count = 0
for i in range(1, n + 1):
    if dl(i) % 2 == 0:
        count += 1

print(count)
