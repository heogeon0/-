delta = [[1,0],[0,1],[-1,-1]]


def solution(n):
    arr = [[0] * n for _ in range(n)]
    ni = nj = d = 0

    num = 1
    while True:
        arr[ni][nj] = num
        num += 1
        cnt = 0
        while cnt<3:
            if 0<=ni+delta[d][0]<n and 0<=nj+delta[d][1]<n and arr[ni+delta[d][0]][nj+delta[d][1]]==0:
                ni += delta[d][0]
                nj += delta[d][1]
                break
            else:
                d = d+1 if d+1<3 else 0
                cnt += 1

        if cnt == 3: break

    answer = []
    for r in range(n):
        for c in range(r+1):
            answer.append(arr[r][c])

    return answer