import math
from itertools import permutations
from copy import deepcopy
from sys import stdin

input = stdin.readline

delta = [[0,1], [1,0], [0,-1], [-1,0]] # 우, 하, 좌, 상

N, M, K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
cal = [list(map(int,input().split())) for _ in range(K)]


order = list(permutations(range(K)))
answer = math.inf

for no in order:
    narr = deepcopy(arr)

    for idx in no:
        nowCal = [cal[idx][0] -1, cal[idx][1] - 1, cal[idx][2]]

        for i in range(1,nowCal[2]+1):
            rs, re = nowCal[0] - i, nowCal[0] + i
            cs, ce = nowCal[1] - i, nowCal[1] + i

            nr, nc = rs, cs

            temp = narr[nr][nc]

            for d in delta:
                while True:

                    nr = nr + d[0]
                    nc = nc + d[1]

                    if not (rs <= nr <= re and cs <= nc <= ce):
                        nr = nr - d[0]
                        nc = nc - d[1]
                        break

                    else:
                        temp, narr[nr][nc] = narr[nr][nc], temp
    for row in narr:
        answer = min(answer, sum(row))

    # 최솟값계산하여 answer 과 비교


print(answer)