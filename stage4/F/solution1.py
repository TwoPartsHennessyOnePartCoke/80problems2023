# WA, Тест 5: неверный ответ

N = int(input())
slippers_count = {}

c = 0
for i in range(N):
    slipper1 = int(input())
    slipper2 = -slipper1

    if slipper1 not in slippers_count:
        slippers_count[slipper1] = 1
    else:
        slippers_count[slipper1] += 1

    if slipper2 in slippers_count and slippers_count[slipper2] > 0:
        c += 1
        slippers_count[slipper2] -= 1

print(c)