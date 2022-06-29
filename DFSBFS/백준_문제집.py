from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N, M = map(int,input().split())

#. 1 방향 그래프, 진입차수 만들기
arr = [[] for _ in range(1+N)]
inD = [0] * (N+1)

for _ in range(M):
    s, e = map(int,input().split())
    arr[s].append(e)
    inD[e] += 1


# 2. 진입차수가 0인것 부터 큐에 넣기
Q = []
for idx in range(1,N+1):
    if not inD[idx]:
        heappush(Q,idx)

# 3. Q를 통한 위상정렬
answer = []

while Q:
    now = heappop(Q)
    answer.append(now)
    # Q에서 하나씩 제거하면서 연결된 노드들의 진입차수 제거
    for i in arr[now]:
        inD[i] -= 1
        if inD[i] == 0:
            heappush(Q, i)

print(*answer)
