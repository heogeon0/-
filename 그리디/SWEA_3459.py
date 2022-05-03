# 승자예측하기

T = int(input()) + 1

for tc in range(1,T):
    N = int(input())
    print(f'#{tc}', end=' ')
    while N > 3:
        N = N // 2 + 1 # 공격자가 부르고 싶은 수
        N = N // 2 - 1 # 공격자가 부르고 싶은 수를 못부르게 막는 방어자의 수

    if N >= 2 or N==0: # 공격자가 2,3의 수를 시작으로 자신이 원하는 수를 만들 수 있다면 Alice 승
        print('Alice')

    else:
        print('Bob')
