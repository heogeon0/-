def bfs(i, j):
    Q = [[i, j]]
    arr[i][j] = 0
    tmp = 1
    while Q:
        ni, nj = Q.pop(0)

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx, dy = ni + d[0], nj + d[1]
            if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] == 1:
                Q.append([dx, dy])
                arr[dx][dy] = 0
                tmp += 1
    cnt.append(tmp)


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
cnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            bfs(i, j)
print(len(cnt))
for k in sorted(cnt):
    print(k)
