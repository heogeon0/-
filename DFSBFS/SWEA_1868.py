from collections import deque
delta = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]


def change_bfs(ni,nj): # 지뢰판이 공개된 배열로 바꾸기
    tmp = 0
    for d in delta:
        dx, dy = ni + d[0], nj + d[1]
        if 0<=dx<N and 0<=dy<N and arr[dx][dy] == '*':
            tmp += 1

    arr[ni][nj] = tmp


def count_check(nr,nc): # 0이면 들어가서 주변숫자 다 -1로 바꾸기
    Q = deque()
    Q.append([nr,nc])
    arr[nr][nc] = '*'

    while Q:
        ni, nj = Q.popleft()

        for d in delta:
            dx, dy = ni + d[0], nj + d[1]
            if 0<=dx<N and 0<=dy<N:
                if arr[dx][dy] == 0:
                    arr[dx][dy] = '*'
                    Q.append([dx,dy])

                elif arr[dx][dy] != '*':
                    arr[dx][dy] = '*'


T = int(input())+1
for tc in range(1,T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                change_bfs(i,j)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt+= 1
                count_check(i,j)


    for i in range(N):
        for j in range(N):
            if arr[i][j] != '*':
                cnt += 1
    print(f'#{tc} {cnt}')