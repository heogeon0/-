#카드구매하기
N = int(input())
pri_lst = [0] + list(map(int,input().split())) #인덱스 맞추기
max_lst = [pri_lst[0]] + [pri_lst[1]]
# 홀수일때는 전수 +f(1) 이 최대
stand = 1  # 현재까지 단위당 카드 수가 가장 비싼 카드팩의 위치
for i in range(2,N+1):
    now_max = 0
    if (max_lst[stand] + max_lst[i-stand]) < pri_lst[i]: #단위당 카드값이 현재 카드값이 더 크다면 stand 교체
           stand = i
           now_max = pri_lst[i]
    else:
        now_max = max_lst[stand] + max_lst[i-stand]
    max_lst.append(now_max)
print(max_lst[-1])
#
# ####

N = int(input())
pri_lst = [0] + list(map(int,input().split()))
max_lst = [0] * (N+1)
for i in range(1,N+1):
    # 가능한 모든경우의 합 중 max값을 구함
    max_lst[i] = max([pri_lst[j] + max_lst[i-j] for j in range(1,i+1)])
print(max_lst[-1])