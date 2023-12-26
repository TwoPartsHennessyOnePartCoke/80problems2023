# AC, Принята

n = int(input())
cnt = []
sc = dict()

for i in range(n):
    g, s, b = input().split()

    if g not in cnt:
        cnt.append(g)
        sc[g] = [0, 0, 0]

    if s not in cnt:
        cnt.append(s)
        sc[s] = [0, 0, 0]

    if b not in cnt:
        cnt.append(b)
        sc[b] = [0, 0, 0]

    sc[g][0] += 1
    sc[s][1] += 1
    sc[b][2] += 1

sc = sorted(sc.items(), key = lambda x: x[0])
sc = sorted(sc, key = lambda x: x[1], reverse=True)
for i in range(len(sc)):
    print(sc[i][0], str(sc[i][1][0]), str(sc[i][1][1]), str(sc[i][1][2]))
