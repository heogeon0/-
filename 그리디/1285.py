# 동전뒤집기

N = int(input())
arr = [list(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            r, c = 0, 0
            for k in range(N):
                if arr[i][k] == 'T': # 행체크
                    r += 1
                if arr[k][j] == 'T':  # 열쳌크
                    c+= 1
            rprofit = r - (N-r) # 바꾸면 이익이 되는 갯수
            cprofit = c - (N - c)
            if rprofit > cprofit and rprofit > 0:
                for l in range(N):
                    arr[i][l] = 'H' if arr[i][l] =='T' else 'T'
                cnt += 1

            elif cprofit > rprofit and cprofit > 0:
                for l in range(N):
                    arr[l][j] = 'H' if arr[l][j] =='T' else 'T'
                cnt += 1

print(cnt)
'''
                if arr[k][j] == 'T': # 열쳌크
                    c.append([k,j])

'''