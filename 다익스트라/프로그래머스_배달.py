import math
from collections import deque

def solution(N, road, K):
    def dik(s):
        D[s] = 0
        Q = deque([[s,0]])

        while Q:
            nr, nc = Q.popleft()

            for c in R[nr]:
                cost = nc + c[1]
                if D[c[0]] > cost:
                    D[c[0]] = cost
                    Q.append([c[0],cost])

    D = [math.inf] * (N+1)
    R = [[] for _ in range(N+1)]


    for s,e,w in road:
        R[s].append([e,w])
        R[e].append([s,w])
    dik(1)


    return sum([1 if D[i] <=K else 0 for i in range(1,N+1)])

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)