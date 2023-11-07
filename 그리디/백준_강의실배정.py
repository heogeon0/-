from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    s, e = map(int, input().split(' '))
    arr.append([e, s])

arr.sort(key=lambda x: (x[1], x[0]))

heap = [[-1, -1]]
print(arr)
for time in arr:
  print(heap)
  E, S = heappop(heap)

  if E <= time[1]:
    heappush(heap, time)
  
  else :
    heappush(heap, time)
    heappush(heap, [E, S])

print(len(heap))
