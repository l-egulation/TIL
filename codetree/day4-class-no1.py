N, M = map(int, input().split())

arr_a = [list(map(int, input().split())) for _ in range(N)]
arr_b = [list(map(int, input().split())) for _ in range(M)]


total_sum_lst = []

for r in range(M-N+1):
    for c in range(M-N+1):
        current_sum = 0

        for i in range(N):
            for j in range(N):
                current_sum += arr_a[i][j] * arr_b[r+i][c+j]
            
        total_sum_lst.append(current_sum)

ans = max(total_sum_lst)

print(ans)