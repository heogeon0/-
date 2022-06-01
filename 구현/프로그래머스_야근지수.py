# Greedy로 접근

def solution(n, works):
    stand = max(works)
    N = len(works)
    while stand:

        for i in range(N):
            if works[i] == stand:
                works[i] -= 1
                n -= 1
                if n == 0:
                    return sum(i**2 if i > 0 else 0 for i in works)
        stand -= 1

    return 0


print(solution(4,[4,3,3]))