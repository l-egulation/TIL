'''
녹는것은 빙산과 비슷
다만, 주위의 0만큼 녹는게 아니라 0이 있으면 녹는 것
> 그냥 1에서 4방향 탐색해서 0이 하나라도 있으면 녹기 > 1을 0으로 만들기

문제가 되는 로직은 1들 중간에 0이 있는 것
> 1 중간에 있는, 즉 1로 둘러쌓여있는 0을 파악해서 이 0들과 닿아있는 1은 녹지 않게 해야함
>> 1. 1로 둘러쌓여있는 0 파악
>> 2. 그 0들과 닿아있는 1들은 녹지 않게 하기

갇힌 0을 어떻게 판단하는가
> 전에 '단지번호 붙이기' bfs처럼 덩어리 0을 세고, 그 0에 대한 좌표를 뽑아서 그 좌표와 인접한 1(치즈)는 녹이지 않는다?

--------------------------------------------------

내부의 0을 찾아서 제외시키는게 아니라 외부의 0을 찾아서 그 0을 

'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

def bfs_external_air(melt_lst):
    visited = [[False]*M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    # external_air = set()
    # external_air.add((0, 0))

    while queue:
        # 현재 위치 꺼내서 주변 수색
        r, c = queue.popleft()

        # 4방향 탐색
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if area[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    # external_air.add((nr, nc))
                elif area[nr][nc] == 1:
                    visited[nr][nc] = True
                    melt_lst.append((nr, nc))

    return visited

hours = 0
last_cheese_count = 0

cheese_lst = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            cheese_lst.append((i, j))

while True:
    if not cheese_lst:
        break

    last_cheese_count = len(cheese_lst)
    melt_lst = []
    bfs_external_air(melt_lst)

    # melt_lst = []
    # for r, c in cheese_lst:
    #     for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    #         if external_air[r+dr][c+dc]:
    #             melt_lst.append((r, c))
    #             break

    for mr, mc in melt_lst:
        area[mr][mc] = 0

    cheese_lst = [(r, c) for r, c in cheese_lst if area[r][c] == 1]

    hours += 1

print(hours)
print(last_cheese_count)