
N = int(input())
myClass = list(map(int,input().split()))

A, B = map(int,input().split())
cnt = 0 # 감독관의 수


for i in range(N):
    total = myClass[i]
    # 1. 메인감독관 여부 결정
    cnt += 1
    total -= A

    if total > 0:
        cnt += total // B
        if total % B :
            cnt += 1

print(cnt)







