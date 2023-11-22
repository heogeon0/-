from collections import deque
from sys import stdin
input = stdin.readline

def bfs(i):
    Q = deque([i])
    v[i] = 1

    while Q:
        ni = Q.popleft()

        for j in range(1,N+1):
            if arr[ni][j] and not v[j]:
                Q.append(j)
                v[j] = 1



N, E = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a, b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1

v = [0] * (N+1)
cnt = 0
for i in range(1,N+1):
    if not v[i]:
        cnt += 1
        bfs(i)

print(cnt)