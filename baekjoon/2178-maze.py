import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]

graph[0][0] = 1
queue = deque([(0, 0)])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

print(graph[N-1][M-1])