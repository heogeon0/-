from collections import deque
def dfs(i):
    v = [0] * (N+1)
    stack = [i]
    while stack:
        ni = stack.pop()

        if not v[ni]:
            print(ni, end=' ')
            v[ni] = 1

            for j in range(N,0,-1):
                if arr[ni][j]:
                    stack.append(j)


def bfs(i):
    print(i, end =' ')
    v = [0] * (N+1)
    Q = deque([i])
    v[i] = 1
    while Q:
        ni = Q.popleft()

        for j in range(N+1):
            if arr[ni][j] and not v[j]:
                print(j, end =' ')
                v[j] = 1
                Q.append(j)


a = set()
a.add(1)
a.add(2)
print(a)
a.discard(2)
print(a)