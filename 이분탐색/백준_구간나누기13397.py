def f(mid):
    global answer
    ncnt = 1
    now_min = 10000
    now_max = 0
    for i in range(N):
        now_min = min(now_min, lst[i])
        now_max = max(now_max, lst[i])

        if now_max - now_min > mid:
            ncnt += 1
            now_min = now_max = lst[i]

    return M >= ncnt


N, M = map(int,input().split())
lst = list(map(int,input().split()))
answer = 10000
left, right = 0, max(lst)

while left <= right:
    middle = (left+right)//2

    if f(middle):
        right = middle - 1
        answer = min(middle, answer)
    else:
        left = middle + 1

print(answer)



