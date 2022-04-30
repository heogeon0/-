# 이친수
dp = [[0,1],[1,0]] + [[0,0] for _ in range(90)]
N = int(input())
for i in range(2,N):
    dp[i][0] = dp[i][1] = dp[i-1][0] # 마지막 0 은 다음 0과 1
    dp[i][0] += dp[i-1][1] # 마지막 1은 다음 0

print(sum(dp[N-1]))

