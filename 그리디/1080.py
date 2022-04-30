


N, M = map(int,input().split())
arr_1 = [list(map(int,list(input()))) for _ in range(N)]
arr_2 = [list(map(int,list(input()))) for _ in range(N)]
arr = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr_1[i][j] != arr_2[i][j]:
            arr[i][j] = 1

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            try:
                for r in range(3):
                    for c in range(3):
                        arr[i+r][j+c] = 1 if arr[i+r][j+c] == 0 else 0
                cnt += 1
            except IndexError:
                print(-1)
                exit()
print(cnt)


