# 회의실 배정
from sys import stdin
input = stdin.readline
N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
table.sort(key=lambda x:(x[1],x[0]),reverse=True)
cnt = stand = 0
while table:
    s, e = table.pop()
    if s >= stand:
        cnt += 1
        stand = e
print(table)
