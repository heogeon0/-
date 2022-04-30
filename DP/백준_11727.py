# 타일문제 2
def tile(n):
    if memo[n]:
        return memo[n]
    else:
        if not memo[n]:
            memo[n] = 2 * tile(n-2) + tile(n-1)
            return memo[n]


n = int(input())
memo = [1] * 2 + [0] * (n-1)
print(tile(n)%10007)