import math
from sys import stdin

input = stdin.readline


N = int(input())
M = int(input())

arr = [[math.inf] * (N+1) for i in range(N+1)]

for _ in range(M):
    s, e, c = map(int,input().split())
    arr[s][e] = min(c, arr[s][e])

for k in range(1,N+1):
    for s in range(1,N+1):
        for e in range(1,N+1):
            arr[s][e] = min(arr[s][e], arr[s][k] + arr[k][e])

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            arr[i][j] = 0
        if arr[i][j] == math.inf:
            arr[i][j] = 0

for i in range(1,N+1):
    for j in range(1, N+1):
        print(arr[i][j], end=' ')
    print('')