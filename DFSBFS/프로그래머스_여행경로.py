def solution(tickets):
    # 모든 도시를 방문하는 방법을 찾는 함수
    def dfs(now):
        nonlocal answer
        # 종료조건 : 모든 티켓을 사용확인
        if sum(v) == N:
            # 알파벳 순서 확인
            if ''.join(answer) >= ''.join(route):
                answer = route[:]
            return

        # 티켓 확인
        for t_idx in range(N):
            if tickets[t_idx][0] == now and not v[t_idx]:
                v[t_idx] = 1
                route.append(tickets[t_idx][1])
                dfs(tickets[t_idx][1])
                route.pop()
                v[t_idx] = 0

    # 1.변수생성
    N = len(tickets)
    v = [0] * N
    route = ["ICN"]
    answer = ["ZZZ"]
    # 2. DFS로 정답찾기
    dfs("ICN")
    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])




