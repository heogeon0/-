# 2458
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())


arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    small, big = map(int,input().split())
    arr[big][small] = 1 # 행을 기준으로 작은것들의 갯수


for k in range(1,N+1):
    for s in range(1,N+1):
        if k==s:
            continue
        for g in range(1,N+1):
            if g==s:
                continue
            cnt = 0
            if arr[k][s] and arr[g][k]: # k가 g와 비교된적이 있고 k가 더 작고, k와 s가 비교된적 있고 s가 더작다면
                cnt = 1  # s는 g보다 작다

            arr[g][s] = max(arr[g][s], cnt)


answer = 0
for i in range(1,N+1):
    scnt = sum(arr[i])
    rcnt = sum([1 if arr[j][i] else 0 for j in range(1,N+1)])
    if scnt + rcnt == N-1:
        answer += 1

print(answer)