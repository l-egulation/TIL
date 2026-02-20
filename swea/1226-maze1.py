from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque([])
    visited = [[False]*16 for _ in range(16)]

    visited[r][c] = True
    queue.append((r, c))

    while queue:
        curr_r, curr_c = queue.popleft()

        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
                continue
            if maze[nr][nc] == 1 or visited[nr][nc]:
                continue
            if maze[nr][nc] == 3:
                return 1
        
            visited[nr][nc] = True
            queue.append((nr, nc))
    
    return 0

for tc in range(1, 11):
    input()
    maze = [list(map(int, input())) for _ in range(16)]

    answer = bfs(1, 1)
    print(f'#{tc} {answer}')