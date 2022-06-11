# 1. 이 문제는 힙을 안쓰는게 더  편할것 같다고 생각하고(마땅한 종료조건이 없는것 같음) 다익스트라로 풀려고 생각
# 2. 다익스트라를 돌릴려고 보니 MST인 것 같음
# 3. MST(prim)알고리즘을 했지만 300**2 시간초과 발생
# 4. 그냥 힙을 사용하는게 더 빠른가? 생각으로 힙으로 풀어봄



# prim 을 이용한 풀이
import math
def solution(land, height):
    def f():
        nr, nc = 0,0
        D[nr][nc] = 0

        for _ in range(N**2):
            min_num = math.inf
            for i in range(N):
                for j in range(N):
                    if not v[i][j] and D[i][j] < min_num:
                        min_num = D[i][j]
                        nr, nc = i,j

            v[nr][nc] = 1

            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dx, dy = nr + d[0], nc + d[1]
                if 0<=dx<N and 0<=dy<N and not v[dx][dy]:
                    if D[dx][dy] > abs(land[dx][dy] - land[nr][nc]):
                        D[dx][dy] = abs(land[dx][dy] - land[nr][nc])

    N = len(land)
    v = [[0] * N for _ in range(N)]
    D = [[math.inf] * N for _ in range(N)]
    f()
    answer = sum([D[i][j] if D[i][j] > height else 0 for i in range(N) for j in range(N)])
    return answer


# 힙을이용한 풀이 (굳이 종료조건을 쓰지 않고, visited만 이용해봄)
from heapq import heappop,heappush

def solution(land, height):

    def f():
        nonlocal answer
        sr, sc = 0, 0
        Q = []
        heappush(Q,[0,sr,sc])
        while Q:
            p, nr, nc = heappop(Q)
            if v[nr][nc]:
                continue

            v[nr][nc] = 1
            answer += p

            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dx, dy = nr + d[0], nc + d[1]
                if 0<=dx<N and 0<=dy<N:
                    if abs(land[dx][dy] - land[nr][nc]) > height:
                        heappush(Q,[abs(land[dx][dy] - land[nr][nc]),dx,dy])
                    else:
                        heappush(Q, [0, dx, dy])

    N = len(land)
    v = [[0] * N for _ in range(N)]
    answer = 0
    f()
    print(answer)
    return answer

solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1)
solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3)