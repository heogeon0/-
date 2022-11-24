import collections
import heapq
from collections import defaultdict

def solution(n, edge):
    graph = collections.defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)
    result = [0] * (n+1)

    queue = collections.deque()
    queue.append(1)
    visited[1] = True

    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if not visited[next_node]:
                result[next_node] = result[current_node] + 1
                queue.append(next_node)
                visited[next_node] = True


    max_ = max(result)
    return result.count(max_)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

