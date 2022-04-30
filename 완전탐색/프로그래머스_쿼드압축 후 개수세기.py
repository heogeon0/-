def solution(arr):
    def check(si, sj, ei, ej):
        nonlocal answer
        if si >= ei - 1 or sj >= ej - 1:
            answer[arr[si][sj]] += 1
            return

        mid_i = (ei + si) // 2
        mid_j = (sj + ej) // 2
        stand = arr[si][sj]
        flag = 0

        for i in range(si, ei):
            for j in range(sj, ej):
                if stand != arr[i][j]:
                    flag = 1


        if flag:
            check(si, sj, mid_i, mid_j)
            check(si, mid_j, mid_i, ej)
            check(mid_i, sj, ei, mid_j)
            check(mid_i, mid_j, ei, ej)


        else:
            answer[stand] += 1
    answer = [0] * 2
    si = sj = 0
    ei = ej = len(arr)
    check(si,sj,ei,ej)

    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))