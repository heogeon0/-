# 하나로
import math

def mst():
    total = 0
    u = 0
    D[u] = 0

    for i in range(N):
        # 가중치 최솟값 찾기
        min = math.inf
        for v in range(N):
            if v != u and visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visited[u] = 1
        total += arr[PI[u]][u]

        for v in range(N):
            if visited[v] == 0:
                if arr[u][v] < D[v]:
                    D[v] = arr[u][v]
                    PI[v] = u

    return math.floor(total * E + 0.5)


T = int(input()) + 1
for tc in range(1,T):
    N = int(input())
    D = [math.inf] * N
    visited = [0] * N
    PI = list(range(N))
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())
    arr = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[j][i] = ((X[i]-X[j])**2+(Y[i]-Y[j])**2)  #가중치 기록

    print(f'#{tc} {mst()}')




