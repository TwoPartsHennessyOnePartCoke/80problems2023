# TL, Тест 8: превышение лимита времени

def bfs(it, jt):
    q = []
    q.append((it, jt))
    used[sl][it][jt] = 0
    while len(q) != 0:
        vi, vj = q.pop(0)
        for c in range(4):
            ti = vi + sm_i[c]
            tj = vj + sm_j[c]
            if -1 < ti < n and -1 < tj < m:
                if (used[sl][ti][tj] == -1) and (used[sl][vi][vj] < k):
                    used[sl][ti][tj] = used[sl][vi][vj] + 1
                    q.append((ti, tj))
                    c2[ti][tj] += 1


n, m, k = map(int, input().split())
mas = [[j for j in input()] for i in range(n)]
c1 = 0
for i in range(n):
    c1 += mas[i].count('*')
c2 = [[0] * m for i in range(n)]
used = [[[-1] * m for i in range(n)] for j in range(c1)]
sm_i = [-1, 0, 1, 0]
sm_j = [0, -1, 0, 1]
i_st = []
j_st = []

for i in range(n):
    for j in range(m):
        if mas[i][j] == '*':
            i_st.append(i)
            j_st.append(j)
            c2[i][j] += 1
        if mas[i][j] == '#':
            for sl in range(c1):
                used[sl][i][j] = 1e9

for sl in range(len(i_st)):
    bfs(i_st[sl], j_st[sl])

ans = []
for i in range(n):
    for j in range(m):
        if c2[i][j] == c1:
            ans.append((i, j))

for i in range(n):
    for j in range(m):
        if mas[i][j] == '#':
            print('#', end='')
        elif (i, j) in ans:
            print('?', end='')
        else:
            print('.', end='')
    print()