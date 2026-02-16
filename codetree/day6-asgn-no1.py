import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(M)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False]*(N+1) for _ in range(N+1)]

for r, c in points:
    visited[r][c] = True
    count = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 1 <= nr <= N and 1 <= nc <= N:
            if visited[nr][nc] == True:
                count += 1
        
    if count == 3:
        print(1)
    else:
        print(0)