def dfs(now,parent,cnt):
    if cnt > 3:
        print(1)
        exit()

    for j in line[now]:
        if j != parent and j not in grandpa:
            grandpa.add(parent)
            dfs(j,now,cnt+1)
            grandpa.discard(parent)


N, E = map(int,input().split())

line = [[] for _ in range(N)]
for _ in range(E):
    edge = list(map(int,input().split()))
    line[edge[0]].append(edge[1])
    line[edge[1]].append(edge[0])

grandpa = set()
for i in range(N):
    dfs(i,-1,0)

print(0)


