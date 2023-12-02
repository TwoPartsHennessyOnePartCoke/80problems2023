# WA, Тест 2: неверный ответ

import math

N, A, X, Y, Z = map(float, input().split())
edges = [X, Y, Z]
N = int(N)

n = N - 3
while n > 0:
    edge = math.sqrt(A**2 + edges[-1]**2 - 2*A*edges[-1]*math.cos(2*math.pi/N))
    edges.append(edge)
    n -= 1

for i in range(N-1, 2,-1):
    print(f"{edges[i]:.5f}")