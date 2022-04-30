from collections import deque
import sys
input = sys.stdin.readline


# O(1000 * 2)
M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def bfs():
    K = 0
    while Q:
        ni, nj, K = Q.popleft()

        for d in [[-1,0],[1,0],[0,-1],[0,1]]:
            dx,dy = ni+d[0], nj+d[1]
            if 0<=dx<N and 0<=dy<M and arr[dx][dy] == -2:
                arr[dx][dy] = K+1
                Q.append([dx,dy,K+1])
    print(K)


def tomato(i,j):
    x = deque([[i,j]])
    arr[i][j] = -2
    flag = 0
    while x:
        ni, nj = x.popleft()

        for d in [[-1,0],[1,0],[0,-1],[0,1]]:
            dx,dy = ni+d[0], nj+d[1]
            if 0 <= dx < N and 0 <= dy < M and arr[dx][dy] >= 0:
                if arr[dx][dy] == 1:
                    flag = 1
                else:
                    x.append([dx,dy])
                    arr[dx][dy] = -2

    if not flag:
        print(-1)
        exit()


Q = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append([i,j,0])
        elif arr[i][j] == 0:
            tomato(i,j)

bfs()

# O((1000 * 2)*K)
# K = 1
# check = 0
# while K:
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == K:
#                 check = 1
#                 ni, nj = i, j
#                 for d in [[-1,0],[1,0],[0,-1],[0,1]]:
#                     dx,dy = ni+d[0], nj+d[1]
#                     if 0<=dx<N and 0<=dy<M and not arr[dx][dy]:
#                         arr[dx][dy] = K+1
#     if not check:
#         if sum(arr,[]).count(0) > 0:
#             print(-1)
#         else:
#             print(K-2)
#         break
#     else:
#         K += 1
#         check = 0
