from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

# Prim 알고리즘
def prim():
    global total
    V[1] = 1
    Q = []
    for c in route[1]:
        heappush(Q,c)


    while Q:
        w, idx = heappop(Q)
       if V[idx]:
            continue
        total += w
        V[idx] = 1
        for c in route[idx]:
            if not V[c[1]]:
                heappush(Q,c)

# 1. 변수저장
N, E = map(int,input().split())
route = [[] for _ in range(1+N)] # 간선 그래프
V = [0] * (1 + N) # 방문기록 그래프

for _ in range(E):
    p, c, w = map(int,input().split())
    route[p].append([w,c]) # 힙에 편하기 넣기 위해 가중치가 앞에 저장
    route[c].append([w,p])

total = 0
prim()
print(total)