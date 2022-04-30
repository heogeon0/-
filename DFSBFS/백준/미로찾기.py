def dfs():
    Q = [[0,0,1]]
    arr[0][0] = 0

    while Q:
        ni, nj, cnt = Q.pop(0)

        if ni == (N-1) and nj == (M-1):
            print(cnt)
            exit()

        for d in [[1,0],[-1,0],[0,-1],[0,1]]:
            dx, dy = ni + d[0], nj + d[1]
            if 0<=dx<N and 0<=dy<M and arr[dx][dy]:
                Q.append([dx,dy,cnt+1])
                arr[dx][dy] = 0


N, M = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(N)]
dfs()