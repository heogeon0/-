from collections import deque
def solution(n, s, a, b, fares):
    def my_bfs(num):
        v1 = [max_value] * (n + 1)
        Q = deque([[num,0]])
        v1[num] = 0
        while Q:
            now, nsum = Q.popleft()
            for i in range(1,n+1):
                if arr[now][i] and v1[i] > arr[now][i] + nsum:
                    v1[i] = arr[now][i] + nsum
                    Q.append([i,v1[i]])

        return v1[s] + v1[a] + v1[b]

    max_value = 100000 * n
    arr = [[0] * (n+1) for _ in range(n+1)]

    for x, y, f in fares:
        arr[x][y] = arr[y][x] = f

    return min([my_bfs(i) for i in range(1,n+1)])

print(solution(6,4,6,2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))