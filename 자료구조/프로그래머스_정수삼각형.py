def solution(triangle):
    N = len(triangle)
    ans = [[0] * i for i in range(1,N+1)]
    ans[0] = triangle[0]
    for i in range(N - 1):
        for j in range(len(triangle[i])):
            for k in range(2):
                ans[i+1][j+k] = max(ans[i+1][j+k], ans[i][j]+triangle[i+1][j+k])


    return max(ans[-1])



ans = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

print(ans)
