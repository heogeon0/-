# 장훈이의 높은 선반
from itertools import combinations as combi
T = int(input()) + 1

for tc in range(1,T):
    N, T = map(int,input().split())
    lst = list(map(int,input().split()))
    ans = 1000000
    for i in range(1,N+1):
        combs = combi(lst,i)
        for com in combs:
            ans = sum(com)-T if sum(com)-T < ans and sum(com) >= T else ans

    print(f'#{tc} {ans}')
