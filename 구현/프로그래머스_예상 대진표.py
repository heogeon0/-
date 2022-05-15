def solution(n,a,b):
    def fight(a,b,c):
        nonlocal ans
        if a == b:
            ans = c
            return

        fight((a+1)//2,(b+1)//2,c+1)
    ans = 0
    fight(a,b,0)
    return ans

print(solution(8,4,7))
