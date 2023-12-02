# AC, Принята

N, L = map(int, input().split())
days = list(map(int, input().split()))

mn = mnd = 1000000

for i in range(N - L + 1):
    if days[i] == 0 and days[i + L - 1] == 0:
        total_rain = sum(days[i+1:i+L-1])
        if total_rain < mn:
            mn = total_rain
            mnd = i + 1

if mn == mnd == 1000000:
    mnd = -1

print(mnd)