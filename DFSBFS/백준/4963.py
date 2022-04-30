def bfs(i,j):
    Q = [[i,j]]
    arr[i][j] = 0

    while Q:
        ni, nj = Q.pop(0)

        for d in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]:
            dx, dy = ni + d[0], nj + d[1]
            if 0<=dx<N and 0<=dy<M and arr[dx][dy] == 1:
                Q.append([dx,dy])
                arr[dx][dy] = 0


while True:
    M, N = map(int,input().split())
    if N==0 and M == 0: exit()
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i,j)

    print(cnt)
