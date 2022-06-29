# 플로이드와샬은 시간복잡도 높음

from sys import stdin
input = stdin.readline

def f(now, idx):
    for pre in arr[idx]:
        if not v[now][pre]:
            v[now][pre] = 1
            v[pre][now] = 1
            f(now,pre)


N, M = map(int,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    p, c = map(int,input().split())
    arr[p].append(c)

v = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    v[i][i] = 1
    f(i,i)



answer = sum([1 if sum(v[i]) == N else 0 for i in range(1,N+1)])
print(answer)