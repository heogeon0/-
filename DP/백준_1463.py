# 1로 만들기
def my_count(n,tmp):
    global cnt
    # 종료조건
    if n == 1 and cnt > tmp:
        cnt = tmp
        return

    #가지치기
    if cnt <= tmp:
        return

    # 몸톰
    if n % 2 == 0:
        my_count(n // 2, tmp+1)

    if n % 3 == 0:
        my_count(n // 3, tmp+1)
    my_count(n-1, tmp+1)


N = int(input())
cnt = 999
my_count(N,0)
print(cnt)
