# 정사각형방
from collections import deque

def my_bfs(ni,nj):
    Q = deque([[ni,nj]])
    cnt = 1

    while Q:
        x, y = Q.popleft()

        for d in [[-1,0],[1,0],[0,-1],[0,1]]:
            dx, dy = x + d[0], y + d[1]
            if 0<=dx<N and 0<=dy<N and arr[dx][dy] == arr[x][y] + 1:
                Q.append([dx,dy])
                cnt += 1

    return  arr[ni][nj], cnt


T = int(input()) + 1
for tc in range(1,T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_cnt = 0
    max_idx = 0
    for i in range(N):
        for j in range(N):
            idx, cnt = my_bfs(i,j)
            if max_cnt < cnt:
                max_cnt = cnt
                max_idx = idx
            elif max_cnt == cnt:
                max_idx = min(max_idx,idx)

    print(f'#{tc} {max_idx} {max_cnt}')

