from collections import deque
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

delta = [[-1,0],[1,0],[0,-1],[0,1]]

def get_son(now_row, now_col, now_e):
    v = [[0]* N for _ in range(N)]
    guest = [[0,0,0,0,0,0]]
    stand = 0
    sr, sc = now_row, now_col
    Q = []
    if arr[sr][sc]:
        return [sr,sc, now_e] + arr[sr][sc] + [1]

    else:
        v[sr][sc] = 1
        heappush(Q,[now_e,sr,sc])

    while Q:
        ne, nr, nc = heappop(Q)

        if ne > stand:
            guest.sort(key=lambda x: (-x[-1], x[0], x[1]))
            return guest[0]

        if arr[nr][nc] != (0 and 1):
            stand = ne
            guest.append([nr,nc,ne] + arr[nr][nc] + [1])

        for d in delta:
            dx, dy = nr + d[0], nc + d[1]
            if 0<=dx<N and 0<=dy<N and not v[dx][dy] and arr[dx][dy] != 1:
                v[dx][dy] = 1
                heappush(Q,[ne+1,dx,dy])

    guest.sort(key=lambda x: (-x[-1], x[0], x[1]))
    return guest[0]


def set_son(now_row, now_col, now_e, g_row, g_col):
    # 현재손님 지우기
    v = [[0] * N for _ in range(N)]
    arr[now_row][now_col] = 0
    v[now_row][now_col] = 1

    Q = deque([[now_row,now_col,-now_e]])

    while Q:
        nr, nc, ne = Q.popleft()

        if ne < 0:
            return [0,0,0,0]

        if nr == g_row and nc==g_col:
            ne = ne + (abs(now_e) - ne) * 2
            return [nr, nc, ne, 1]

        for d in delta:
            dx, dy = nr + d[0], nc + d[1]
            if 0<=dx<N and 0<=dy<N and not v[dx][dy] and arr[dx][dy] != 1:
                v[dx][dy] = 1
                Q.append([dx,dy,ne-1])

    return [0, 0, 0, 0]


N, M , ne = map(int,input().split()) # N : 격자크기, M : 승객 수, E : 연료 수
# 0 : 길, 1: 벽, -1 : 방문체크
arr = [list(map(int,input().split())) for _ in range(N)]
nr, nc = map(int,input().split()) # 택시의 위치
nr-=1
nc-=1
for s in range(M):
    r,c,gr,gc = map(int,input().split())
    arr[r-1][c-1] = [gr-1,gc-1]


answer = -1
cnt = 0

while cnt < M:
    nr, nc, ne, gr, gc, f = get_son(nr,nc,-ne)
    if f:
        nr, nc, ne, f = set_son(nr, nc, ne, gr, gc)
        if not f:
            print(-1)
            exit()
        else:
            cnt += 1
    else:
        print(-1)
        exit()

print(ne)










