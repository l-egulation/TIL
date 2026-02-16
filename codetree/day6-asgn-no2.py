N = int(input())
grid = [list(input().strip()) for _ in range(N)]
K = int(input())

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

if 1 <= K <= N:
    r, c, d = 0, K - 1, 2
elif N + 1 <= K <= 2 * N:
    r, c, d = K - N - 1, N - 1, 3
elif 2 * N + 1 <= K <= 3 * N:
    r, c, d = N - 1, 3 * N - K, 0
else:
    # 3 * N + 1 <= K <= 4 * N
    r, c, d = 4 * N - K, 0, 1

bounces = 0

while 0 <= r < N and 0 <= c < N:
    mirror = grid[r][c]
    
    if mirror == '/':
        if d % 2 == 0:
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
    else:
        if d % 2 == 0:
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
    
    bounces += 1
    r += dr[d]
    c += dc[d]

print(bounces)