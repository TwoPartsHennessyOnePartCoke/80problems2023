# WA, Тест 2: неверный ответ

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    mass = []
    x_min = 0
    x_max = 1e10

    temp_fix = list(map(int, input().split()))
    for i in range(n):
        mass.append([temp_fix[i], 0])
        if i == m:
            fix = temp_fix[i]

    temp_perc = list(map(int, input().split()))
    for j in range(n):
        mass[j][1] = temp_perc[j]
        if j == m:
            perc = temp_perc[j]

    for k in range(n):
        fix_diff = fix - mass[k][0]
        perc_diff = mass[k][1] - perc

        if perc_diff == 0:
            if fix_diff <= 0:
                continue
            else:
                x_max = -1
                break

        border = (fix_diff) / (perc_diff) * 100
        if perc_diff >= 0:
            x_min = max(x_min, border)
        else:
            x_max = min(x_max, border)

    if x_max == 1e10:
        print(f'{x_min:.8f}', "INF")
    elif x_max < x_min:
        print("NOT EXISTS")
    else:
        print(f'{x_min:.8f}', f'{x_max:.8f}')
