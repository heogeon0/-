# ATM
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
acc = [0] * N
acc[0] = lst[0]
for i in range(1,N):
    acc[i] = acc[i-1]+lst[i]
print(sum(acc))
