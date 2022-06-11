from heapq import heappop, heappush, heapify

def solution(operations):
    Q = []
    for op in operations:
        m, num = op.split()
        num = int(num)

        if m == 'I':
            heappush(Q, num)

        else:
            if num < 0:
                if Q:
                    heappop(Q)
            else:
                if Q:
                    Q = list(map(lambda x: -x, Q))
                    heapify(Q)
                    heappop(Q)
                    Q = list(map(lambda x: -x, Q))
                    heapify(Q)


    if Q:
        return [max(Q), min(Q)]
    else:
        return [0,0]



print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))