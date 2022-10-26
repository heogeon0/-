

from sys import stdin
from collections import deque

input= stdin.readline

delta = [[-1,0], [0,1], [1,0], [0,-1]]

n, m = map(int, input().split())

board = [list(input().strip()) for _ in range(n)]


visited = [[[[False] * m for _ in range(n) ] for _ in range(m)] for _ in range(n)]
q = deque()



def init():
    rx, ry, bx, by = [0] * 4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j

            elif board[i][j] == 'B':
                bx, by = i, j

    q.append([rx, ry, bx, by, 1])
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    count = 0

    while board[x+dx][y+dy] != '#' and board[x][y] != "O":

        x+= dx
        y += dy
        count += 1

    return x,y,count


def bfs():
    init()

    while q:
        rx,ry, bx, by, depth = q.popleft()

        if depth > 10:
            break

        for i in range(4):
            next_rx, next_ry, r_count = move(rx,ry, delta[i][0], delta[i][1])
            next_bx, next_by, b_count = move(bx, by, delta[i][0], delta[i][1])

            if board[next_bx][next_by] == "O":
                continue

            if board[next_rx][next_ry] == "O":
                print(depth)
                return

            if next_rx == next_bx and next_ry == next_by:

                if r_count > b_count:
                    next_rx -= delta[i][0]
                    next_ry -= delta[i][1]

                else:
                    next_bx -= delta[i][0]
                    next_by -= delta[i][1]


            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth + 1))

    print(-1)

bfs()