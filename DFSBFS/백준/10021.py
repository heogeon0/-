import math

def mst():
    total = 0
    now = 0

    for i in range(N):
        min = math.inf
        flag = 0
        for pre in range(N):
            if now != pre and not v[pre] and D[pre] < min:
                min = D[pre]
                now = pre
                flag = 1

        if not i or flag:
            v[now] = 1
            if i:
                total += min
        else:
            print(-1)
            return

        for pre in range(N):
            if not v[pre]:
                tmp = (table[now][0] - table[pre][0]) ** 2 + (table[now][1] - table[pre][1]) ** 2
                if MIN <= tmp < D[pre]:
                    D[pre] = tmp


    print(total)

N, MIN = map(int,input().split())
v = [0] * N
D = [math.inf] * N
table = []

for i in range(N):
    table.append(list(map(int,input().split())))

mst() # 굳이 부모노드가 필요한가?
