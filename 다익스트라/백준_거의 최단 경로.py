import math
from sys import stdin
from heapq import heappush, heappop
from collections import deque

def dik(S, G, D, R) # 시작점, 목표점, 다익스트라 배열, 활용할 루트
    Q = []
    D[S] = 0
    heappush(Q,[0,S])

    while Q:
        nc, nr = heappop(Q)

        if nr == G:
            return nc

        for c in R[nr]:
            cost = nc + c[1]
            if cost < D[c[0]]:
                D[c[0]] = cost
                heappush(Q,[cost, c[0]])


def bfs(now):
    Q = deque([now])

    while Q:
        n = Q.pop()

        nlen = len(rroute[n])
        # for 문을 순회하면서 삭제하기 위해 반대로 순회함
        for idx in range(nlen-1, -1, -1):
            pre, cost = rroute[n][idx]
            if D[pre] == D[n] - cost:
                Q.append(pre)
                del rroute[n][idx]


input = stdin.readline

while True:
    N, M = map(int,input().split())
    if not (N and M):
        exit()
    S, G = map(int,input().split())

    # 출발점에서 목적지
    route = [[] for _ in range(N)]
    # 목적지에서 출발지
    rroute = [[] for _ in range(N)]

    for _ in range(M):
        p, c, w = map(int,input().split())
        route[p].append([c,w])
        rroute[c].append([p,w])

    D = [math.inf] * N
    dik(S,G,D,route)
    bfs(G)
    D = [math.inf] * N
    dik(G,S,D,rroute)
    print(D[S] if D[S] != math.inf else -1)
