# AC, Принята

hn = int(input()) // 2

for z in range(0, hn + 1):
    x = (hn - z) / 3
    if round(x) == x:
        ans = 4 * x
        print(int(ans))
        break
