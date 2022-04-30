# 자기방으로 돌아가기

T = int(input()) + 1

for tc in range(1,T):
    N = int(input())
    # 통로에 곂치는 횟수가 필요 시간이므로 통로의 방문횟수를 기록
    ans_lst = [0] * 200

    for _ in range(N):
        sr, er = map(int,input().split())
        # 방번호가 1~2 번방인경우 ans_list[0] 에 방문 체크가 되도록 조정
        sr = (sr-1) // 2
        er = (er-1) // 2

        # 시작방에서 목표방으로 가는 통로에 방문체크
        for i in range(min(sr,er),max(sr,er)+1):
            ans_lst[i] += 1
    # 방문이 가장 많이 곂치는 곳이 걸리는 시간간
    print(f'#{tc} {max(ans_lst)}')
