# STN / SRT
from heapq import heappop, heappush

def solution(jobs):
    jobs.sort(key=lambda x:(x[0],x[1]))
    Q = []
    N = len(jobs)
    now = total = flag = 0

    while jobs:
        if not flag:
            if jobs[0][0] <= now:
                intime, time = jobs.pop(0)
                now = now + time
                total += now - intime
                flag = 1
            else:
                now += 1

        else:
            if jobs[0][0] <= now:
                temp = jobs.pop(0)
                heappush(Q,[temp[1],temp[0]])
            else:
                if Q:
                    time, intime = heappop(Q)
                    now += time
                    total += now - intime
                else:
                    now += 1
                    flag = 0

    while Q:
        time, intime = heappop(Q)
        now += time
        total += now - intime

    answer = total//N
    return answer


solution([[0, 10], [4, 10], [15, 2], [5, 11]])


