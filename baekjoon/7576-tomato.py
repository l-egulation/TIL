import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue = deque([])

for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            start_r = r
            start_c = c
            queue.append((start_r, start_c))
            visited[r][c] = 1

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

ans = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0 and visited[r][c] == 0:
            print(-1)
            exit()
        
        ans = max(ans, visited[r][c])

print(ans - 1)