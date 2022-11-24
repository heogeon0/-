from sys import stdin
from collections import deque
input = stdin.readline


# delta = [[], [], [[0,1,2],[1,1,3]], [[0,1,2],[1,1,3],[1,0,4]],[[1,0,4,],[1,1,3]]]
# # 2 : 가로 , 3 :대각선, 4 : 세로
# N = int(input())
#
# Map = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N) ] + [[1] * (N+2)]
#
# cnt = 0
#
# def brut(er, ec, dr):
#     global cnt
#     if er == N and ec == N:
#         cnt += 1
#         return
#
#     next_directions = delta[dr]
#     for nd in next_directions:
#         ner, nec = er + nd[0], ec+nd[1]
#         if not Map[ner][nec]:
#             if nd[2] == 3:
#                 if not Map[ner -1][nec] and not Map[ner][nec - 1]:
#                     brut(ner, nec, nd[2])
#             else:
#                 brut(ner, nec, nd[2])
#
#
# def bfs(er, ec, dr):
#     global cnt
#     Q = deque([[er,ec,dr]])
#
#     while Q:
#         nr, nc, nd = Q.popleft()
#         if nr == N and nc == N:
#             cnt += 1
#
#         else:
#             next_directions = delta[nd]
#             for nnd in next_directions:
#                 ner, nec = nr + nnd[0], nc + nnd[1]
#                 if not Map[ner][nec]:
#                     if nnd[2] == 3:
#                         if not Map[ner - 1][nec] and not Map[ner][nec - 1]:
#                             Q.append([ner, nec, 3])
#
#                     else:
#                         Q.append([ner, nec, nnd[2]])
#
#
#
# bfs(1,2,2)

# DP 해결
def solution():
    # 1행 미리 처리하기 → (3) 과정
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()