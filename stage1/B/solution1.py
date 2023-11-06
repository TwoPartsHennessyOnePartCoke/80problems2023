# AC, Принята

x, y, z, w = map(int, input().split())

count = 0
for i in range(0, w//x + 1):
    w1 = w - i*x
    for j in range(0, w1//y + 1):
        w2 = w1 - j*y
        if w2 % z == 0:
            count += 1

print(count)
