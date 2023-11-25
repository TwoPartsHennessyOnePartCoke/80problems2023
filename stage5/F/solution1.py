# AC, Принята
n, m, s = map(int, input().split())

folders = [0 for i in range(n)]

for i in range(m):
    place, size = map(int, input().split())
    lost = 0 if (size % s == 0) else (s - size % s)
    folders[place] += lost

for i in range(n):
    print(folders[i])
