from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    visited = [[0]*16 for _ in range(16)]

    visited[r][c] = 1
    q.append((r, c))

    # q가 비어있을땐 False 처리가 되서 q가 비어있을 때까지 돔
    while q:
        r, c = q.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
                continue
            if graph[nr][nc] == 1 or visited[nr][nc]:
                continue
            if graph[nr][nc] == 3:
                return 1
            
            visited[nr][nc] == 1
            q.append((nr, nc))

    # 출구를 발견하지 못했을 때
    return 0

T = 10

for tc in range(1, T+1):
    input()
    graph = [list(map(int, input())) for _ in range(16)]
    r, c, goal_r, goal_c = -1, -1, -1, -1
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                r = i
                c = j
            elif graph[i][j] == 3:
                goal_r = i
                goal_c = j

    answer = bfs(r, c)
    print(f'#{tc} {answer}')