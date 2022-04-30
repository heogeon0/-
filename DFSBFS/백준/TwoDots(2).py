from collections import deque

delta = [[0,1],[1,0],[0,-1],[-1,0]]

def bfs(i,j, flag, dr):
    Q = deque([[i,j,dr]])
    v[i][j] = 5

    while Q:
        ni, nj, dr = Q.popleft() # dr : 몇 번 방향으로 왔는지.
        for d in range(4):
            dx, dy = ni+delta[d][0], nj + delta[d][1]
            if 0<=dx<N and 0<=dy<M and arr[dx][dy] == flag:
                if not v[dx][dy]:
                    v[dx][dy] = v[ni][nj] + d
                    Q.append([dx,dy,d])

                elif v[dx][dy] != v[ni][nj] - dr: #내가 온방향이 아니면
                    print('Yes')
                    exit()


N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
v = [[0] * M for i in range(N)]


for i in range(N):
    for j in range(M):
        if not v[i][j]:
            bfs(i,j, arr[i][j],0)

print('No')