from collections import deque

def solution(n, computers):
    def BFS(k):
        nonlocal answer
        answer += 1
        Q = deque([k])
        while Q:
            nr = Q.popleft()

            for nc in range(0, n):

                if computers[nr][nc] and not v[nc]:
                    v[nc] = 1
                    Q.append(nc)

    v = [0] * n
    answer = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] and not v[j]:
                BFS(i)

    print(answer)
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

solution(n,computers)