'''
단지를 구별하는 기준이 필요
1을 찾았다면 방문처리, 그리고 집 개수 카운트 +1
그리고 4방향으로 탐색하고 다음으로 1이 있는 좌표?를 큐에 넣음
찾은 1 쪽으로 이동 > 큐에 넣으면 이동한 것
그리고 인접한 쪽에 1을 모두 방문했고, 더이상 방문할 1이 없다면 0으로 이동 후 단지 수 카운트 +1
집 개수 카운트는 0으로 초기화

총 단지 수가 얼마인지 모르니까
딕셔너리 형태가 필요할 듯
그때 그때 get으로 단지 key 추가하고 해당 value로 집 개수 넣기
'''
import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_count(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1
    count = 1

    while queue:
        curr_r, curr_c = queue.popleft()
        
        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    count += 1
    
    return count

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            complex_count = bfs_count(i, j)
            result.append(complex_count)

result.sort()
print(len(result))
for answer in result:
    print(answer)