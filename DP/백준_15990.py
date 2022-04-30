from sys import stdin
input = stdin.readline
lst = [[1,0,0]] + [[1,0,0]] + [[0,1,0]] + [[0,0,0] for _ in range(100001)]
# 각행의 마지막 수 기록

for i in range(3, 100001):
    lst[i][0] = (lst[i - 1][1] + lst[i - 1][2]) % 1000000009
    lst[i][1] = (lst[i - 2][0] + lst[i - 2][2]) % 1000000009
    lst[i][2] = (lst[i - 3][0] + lst[i - 3][1]) % 1000000009

for _ in range(int(input())):
    N = int(input())
    print(sum(lst[N]) % 1000000009)


