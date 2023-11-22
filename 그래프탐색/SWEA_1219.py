# 길찾기

def bfs():
    v[0] = 1
    q = [0]

    while q:
        now = q.pop(0)
        if now == 99:
            return 1
        for i in range(100):
            if not v[i] and arr[now][i]:
                q.append(i)
                v[i] = 1
    return 0

for tc in range(1,11):
    tc, N = map(int,input().split())
    v = [0] * 100
    lst = list(map(int,input().split()))
    arr = [[0]*100 for _ in range(100)]
    for i in range(N):
        s, e = lst[i*2], lst[i*2+1]
        arr[s][e] = 1

    sol = bfs()
    print(f'#{tc} {sol}')