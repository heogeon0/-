# 현재 위치에서 가장 멀리가는 법 구하기
from collections import deque
from sys import stdin
input = stdin.readline


def dik(s):
    Q = deque([[s,0]]) # 현재위치와 현재까지 시간

    while Q:
        nr, ns = Q.popleft()

        for c in route[nr]:
            cost = ns + c[1]
            if D[c[0]] < cost:
                D[c[0]] = cost
                Q.append([c[0],cost]) # 다음위치, 다음위치까지 시간


def bfs(s, c):
    global answer_cnt
    Q = deque([[s,c]]) #도착지, 도착지까지의 비용

    while Q:
        nr, nc = Q.popleft()

        llen = len(rroute[nr])
        for idx in range(llen-1, -1,-1):
            pre, cost = rroute[nr][idx]
            if D[pre] == nc - cost:
                Q.append([pre,D[pre]])
                answer_cnt += 1

                del rroute[nr][idx]


N = int(input())
M = int(input())
route = [[] for _ in range(N+1)]
rroute = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int,input().split())
    route[s].append([e,w])
    rroute[e].append([s,w])

S, E = map(int,input().split())

# 1. 다익스트라를 활용하여 도착도시까지 갔을 떄 가장 큰 비용을 구한다(답1)
D = [0] * (N+1)
dik(S)
answer_cost = D[E]

# 2. bfs를 활용하여 가장 큰 비용으로 오는 도로의 갯수를 샌다
answer_cnt = 0
bfs(E,answer_cost)
print(f'{answer_cost}\n{answer_cnt}')


