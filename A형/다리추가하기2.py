from collections import deque, defaultdict
from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

delta = [[-1,0],[1,0],[0,-1],[0,1]]

N, M = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]

number = 2

def land(r, c):
    Q = deque([[r,c]])

    while Q:
        nr, nc = Q.popleft()
        maps[nr][nc] = number

        for dr, dc in delta:
            nnr = nr + dr
            nnc = nc + dc
            if 0 <= nnr < N and 0 <= nnc < M and maps[nnr][nnc] == 1:
                Q.append([nnr,nnc])


def bridge(nr, nc, nd, id):
    Q = deque([[0, nr, nc]])

    while Q:
        cnt, nr, nc= Q.popleft()

        if maps[nr][nc] != id and maps[nr][nc] != 0:
            if cnt > 2:
                route[id].append([cnt - 1,maps[nr][nc] ])
            return

        nnr = nr + delta[nd][0]
        nnc = nc + delta[nd][1]

        if 0<=nnr < N and 0 <= nnc < M and maps[nnr][nnc] != id:
            Q.append([cnt+1, nnr, nnc ])

def prim():
    total = 0
    v[2] = 1
    Q = []

    for child in route[2]:
        heappush(Q, child)

    while Q:
        w, idx = heappop(Q)
        if v[idx]:
            continue

        v[idx] = 1
        total += w

        for c in route[idx]:
            if not v[c[1]]:
                heappush(Q,c)

    return total if sum(v) == number - 2 else -1

for r in range(0, N):
    for c in range(0, M):
        if maps[r][c] == 1:
            land(r,c)
            number += 1

# 길 잇기
route = defaultdict(list,{})
for r in range(0, N):
    for c in range(0, M):
        if maps[r][c]:
            for idx in range(4):
                bridge(r, c, idx, maps[r][c])

# MST 알고리즘

v = [0] * number

total = prim()

print(total)

