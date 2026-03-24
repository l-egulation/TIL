'''
단지 몇 갠지 세기

근데 input 받는게 좀 특이?
r, c를 띄어쓰기로 주니까 area 0으로 다 만들어넣고, input for문으로 받아서 그 좌표를 1로 바꾸기
> 아 근데 뭔가 그 거리재는걸로 굳이 area 안그리고 될 거 같은데..?
'''
from collections import deque

def bfs(R, C):
    queue = deque([(R, C)])
    visited[R][C] = True

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if area[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    area = [[0]*M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        # if 0 <= a < M and 0 <= b < N:
        area[b][a] = 1

    visited = [[False]*M for _ in range(N)]

    answer = 0

    for r in range(N):
        for c in range(M):
            if area[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                answer += 1

    print(answer)