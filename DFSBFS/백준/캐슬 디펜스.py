from itertools import combinations
from collections import deque
from copy import  deepcopy
delta = [[0,-1], [-1,0], [0,1]] # 좌, 상, 우
N, M, D = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
arr.append([3] * M)

def archor(now, maps, flag, target):
    Q = deque([[N,now,0]])

    while Q:

        nr, nc, cnt = Q.popleft()

        if cnt > D:
            return

        if maps[nr][nc] == 1:
            target.add((nr, nc))
            return

        if maps[nr][nc] != 3:
            maps[nr][nc] = flag


        for d in delta:
            nextr, nextc = nr + d[0], nc + d[1]
            if 0 <= nextr < N and 0<= nextc <M and maps[nextr][nextc] != flag and maps[nextr][nextc] != 3:
                Q.append([nextr, nextc, cnt + 1])

    return


def monster(maps, target):

    flag = 9
    for row in range(N-1, -1, -1):
        for col in range(M):
            if (row, col) in target:

                maps[row][col] = 0

            else:
                if maps[row][col] == 1:
                    flag = 0

                    if row != N-1:
                        maps[row+1][col] = 1
                maps[row][col] = 0

    if flag == 9:
        return 3
    return 0



def game(position):
    catch = 0
    maps = deepcopy(arr)

    # 1-2-1. 궁수가 활을 쏘는 턴
    # 각각의 궁수가 가까운 곳 부터 활을 쏨
    while True: # 게임이 끝나기 전까지
        target = set()
        for i in range(1,4):
            archor(position[i-1], maps, i * 10, target)


        catch += len(target)

    # 1-2-2. 몬스터가 내려오는턴
        res = monster(maps,target)

    # # 1-3. 최대 몬스터 계산 밑 궁스들 위치 새로 결정
        if res:
            if res == 3:
                return catch
            break

    return catch


# 1-1. 궁수들의 위치결정
positions = combinations(range(M), 3)

# 1-2. 궁수들의 위치로 게임시작
answer = 0
for position in positions:

    if position:
        answer = max(answer,game(position))

print(answer)
