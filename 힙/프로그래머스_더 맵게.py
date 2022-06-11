import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        if scoville[0] < K:
            if len(scoville) < 2:
                return -1

            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)

            c = a + b * 2
            heapq.heappush(scoville,c)
            answer += 1
        else:
            return answer
