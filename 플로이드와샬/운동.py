import math
from sys import stdin
input = stdin.readline

V, E = map(int,input().split())

D = [[math.inf] * (V+1) for _ in range(V+1)]

for _ in range(E):
    r, c, w = map(int,input().split())
    D[r][c] = w

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            D[a][b] = min(D[a][b], D[a][k] + D[k][b])

answer = []
for a in range(1,V+1):
    answer.append(D[a][a])

print(min(answer) if min(answer) < math.inf else -1)