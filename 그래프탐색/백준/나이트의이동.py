from collections import deque

def dfs(r,c):
    Q = deque([[r,c,0]])
    arr[r][c] = 1

    while Q:
        ni, nj, cnt = Q.popleft()
        if ni == tr and nj == tc:
            print(cnt)
            return

        for d in [[-2,-1],[-2,1],[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]:
            dx, dy = ni + d[0], nj + d[1]

            if 0<=dx<N and 0<=dy<N and not arr[dx][dy]:
                Q.append([dx,dy,cnt+1])
                arr[dx][dy] = 1



T = int(input()) + 1
for tc in range(1,T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    r, c = map(int,input().split())
    tr, tc = map(int,input().split())
    dfs(r,c)