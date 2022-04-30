#123더하기
def f(n,flag):
    global ans
    #정지조건
    if n == 0:
        ans += 1
        return

    if n >= 3: f(n-3,1)
    if n >= 2: f(n-2,1)
    f(n-1,1)

for tc in range(int(input())):
    N = int(input())
    ans = 0
    f(N,1)
    print(ans)
