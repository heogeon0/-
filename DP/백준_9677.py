N = int(input())

DP = [0] * (N + 1)
# 상근이가 이기는 경우 : 0, 창완이가 이기는 경우 : 1

print('SK' if N % 2  else 'CY')