from sys import stdin
input = stdin.readline
# 동전 0 (완전탐색 시 메모리초과) (가치가 배수관계인걸 못봤음.. .ㅠ)
# import sys
# sys.setrecursionlimit(10**6)
#
# def heo(value, cnt, yaho):  # 마지막으로 사용된 동전단위
#     global ans
#     if cnt >= ans:
#         return
#
#     if value == 0:
#         ans = cnt
#         for i in range(yaho+1,N):
#             v[i] = 1
#         return
#
#     for i in range(N):
#         if not v[i]:
#             tmp = value - cash[i]
#             if tmp >= 0:
#                 heo(tmp,cnt+1,0)
#

# 돈의 가치가 그리디이기 때문에 그리디 접근 가능
N, target = map(int,input().split())
cash = [int(input()) for _ in range(N)]
ans = 0
i = -1
while target > 0:
    if target >= cash[i]:
        ans += target//cash[i]
        target -= target//cash[i] * cash[i]
    else:
        i -= 1
    if target == 0:
        break
print(ans)