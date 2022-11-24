import itertools
import math
from collections import defaultdict, deque
from copy import deepcopy
from sys import stdin

input = stdin.readline

N = int(input())
peo = [0] + list(map(int,input().split()))
sumpeople = sum(peo)

maps = defaultdict(list)

for i in range(1, N+1):
    friends = list(map(int,input().split()))
    for idx in range(1, friends[0]+1):
        maps[i].append(friends[idx])




# 2. BFS를 활용하여 두개의 지역구로 나눠지는지 검증
# def bfs(v):
#     newv = deepcopy(v)
#     NQ = deque()
#     for i in range(1, N+1):
#         if not newv[i]:
#             newv[i] = 1
#             NQ.append(i)
#             break
#
#     while NQ:
#         now = NQ.popleft()
#
#         for child in maps[now]:
#             if not newv[child]:
#                 newv[child] = 1
#                 NQ.append(child)
#
#     if sum(newv[1:]) == N:
#         return 1
#     return 0

def bfs(lst):
    snow = lst[0]
    Q = deque([snow])
    v = set([snow])
    _sum = 0

    while Q:
        now = Q.popleft()
        _sum += peo[now]

        for child in maps[now]:
            if child not in v and child in lst:
                Q.append(child)
                v.add(child)

    return _sum, len(v)




# 1. 재귀를 통한 완전탐색
# def sol(now, n, total, pa):
#     global answer
#     if n == N: # 두 선거구로 못나누는 경우
#         return
#
#     if abs((sumpeople - total) - total) <= answer:
#         flag = bfs(v)
#
#         if flag:
#             answer = abs((sumpeople - total) - total)
#
#     for child in maps[now]:
#         if not v[child]:
#             v[child] = 1
#             sol(child, n+1, total + peo[child], now)
#             v[child] = 0
#
#     for child in maps[pa]:
#         if not v[child]:
#             v[child] = 1
#             sol(child, n+1, total + peo[child], now)
#             v[child] = 0
#
#


answer = math.inf
for i in range(1,N//2 +1):
    combis = list(itertools.combinations(range(1,N+1),i))

    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(1,N+1) if i not in combi])

        if v1 + v2 == N:
            answer = min(answer, abs(sum1-sum2))



    # while Q:
    #     now, cnt, total = Q.popleft()
    #
    #     v[now] = 1
    #     if cnt == N:
    #         break
    #
    #     if abs((sumpeople - total) - total) <= answer:
    #         flag = bfs(v)
    #
    #         if flag:
    #             answer = abs((sumpeople - total) - total)
    #
    #     for child in maps[now]:
    #         if not v[child]:
    #             Q.append([child,cnt+1,total+peo[child]])

print(answer if answer != math.inf else -1)