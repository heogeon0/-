# 전구와 스위치
N = int(input())
now = [0]*2 + list(map(int,list(input()))) + [0]*2
target = [0]*2 + list(map(int,list(input()))) + [0]*2
cnt = [0,0]
for i in range(1,N+1):
    if now[i-1:i+2] != target[i-1:i+2]:
        now[i-1], now[i], now[i+1] = map(lambda x: 1 if x == 0 else 0, now[i-1:i+2])
        cnt[k] += 1

print(min(cnt) if now[1:N+1] == target[1:N+1] else -1)
