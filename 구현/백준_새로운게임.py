delta = [[0], [0,1],[0,-1],[-1,0],[1,0]]
opp = [[0], [2], [1], [4], [3]]

N, SN = map(int,input().split())

arr = [[2]*(N+1)]
for i in range(N):
    arr.append([2] + list(map(int,input().split())) + [2])
arr.append([2]*(N+1))

table = [[[] for j in range(N+1)] for i in range(N+1)]
stone = [[0]]
for i in range(1,SN+1):
    r, c, d = map(int,input().split())
    stone.append([r,c,d])
    table[r][c].append(i)

## 코드 시작

for i in range(1,1001):

    for j in range(1,SN+1):
        nr, nc, nd = stone[j]
        if table[nr][nc][0] == j:
        ## 움직이기
            dr, dc = nr + delta[nd][0], nc + delta[nd][1]
            # 색깔 확인 (1. 빨간색, 2.파란색)
            if arr[dr][dc] == 2:
                nd = opp[nd][0]
                dr, dc = nr + delta[nd][0], nc + delta[nd][1]
                if arr[dr][dc] == 2:
                    stone[j] = [nr, nc, nd]
                else:
                    if arr[dr][dc] == 0:  # 색깔이 없다면 그대로 더하고
                        table[dr][dc] += table[nr][nc]
                    else:  # 색깔이 있다면 뒤집어서 더한다
                        table[dr][dc] += table[nr][nc][::-1]
                    stone[j] = [dr, dc, nd]
                    table[nr][nc] = []  # 다 한 이후에 이전위치를 지운다

                    # 작업이 끝난 후 종료조건을 확인하고 스톤정보를 최신화 한다
                    if len(table[dr][dc]) >= 4:
                        print(i)
                        exit()
                    for k in range(1, SN + 1):
                        if stone[k][0] == nr and stone[k][1] == nc:
                            stone[k] = [dr, dc, stone[k][2]]

            else: # 다른색깔이라면 일단 움직여야한
                if arr[dr][dc] == 0: # 색깔이 없다면 그대로 더하고
                    table[dr][dc] += table[nr][nc]
                else: # 색깔이 있다면 뒤집어서 더한다
                    table[dr][dc] += table[nr][nc][::-1]
                stone[j] = [dr, dc, nd]
                table[nr][nc] = [] # 다 한 이후에 이전위치를 지운다

            # 작업이 끝난 후 종료조건을 확인하고 스톤정보를 최신화 한다
                if len(table[dr][dc]) >= 4:
                    print(i)
                    exit()
                for k in range(1,SN+1):
                    if stone[k][0] == nr and stone[k][1] == nc:
                        stone[k] = [dr,dc,stone[k][2]]



print(-1)



