# AC, Принята

n, d = map(int, input().split())

def to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

times = []

for i in range(n):
    times.append(to_seconds(input()) - i * 60)

times.sort()

for i in range(1, n + 1):
    for j, k in zip(times, times[i:]):
        if k - j < d:
            break
    else:
        print(i)
        break
    continue
