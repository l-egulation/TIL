'''
최단거리를 측정하는 문제라고 생각

N, M이 행과 열, 즉 세로와 가로에 해당됨
> 원래 자주 나왔던 NxN처럼 정사각형이 아니라서 graph를 순회할 때 유의해야함

근데 node가 아닌 행렬 형태(2차원 리스트)를 순회해야되는데 어떻게 함?
> queue에도 좌표가 들어가나?
> 튜플로 queue에 들어감
>> 튜플로 (r, c)형태로 넣어서 각각 언패킹해서 변수에 할당하면 그 지점으로 이동 가능

그냥 단순히 반대편까지 최단거리라고 생각했으나 테스트케이스를 보면 출발지(익은 토마토, 1)가 여러 개임
> 컴퓨터는 동시동작을 못하는데 어떻게 측정해야하나?
> 동시 동작은 못하지만 BFS로 queue에 넣을 때, 1의 좌표가 하나씩 들어감
>> 그래서 결국 한 지점씩 차근차근 진행하면서 queue에 넣고 하다보면 출발지가 여러 개 일지라도 가능함 

과연 거리 측정은 어떻게 하는가?
> 도저히 방법이 안떠올라서 Gemini에게 도움을 청함
> visited를 True&False 말고 정수 형태로 하는데, BFS하면서 +1씩 하는 것, 말로는 어려워서 그림으로
0 0 0        0 0 0        0 0 3
0 0 0   ->   0 0 2   ->   0 3 2
0 0 1        0 2 1        3 2 1
> 이런 식으로 근처(다른 곳)를 방문 할때마다 visited에 방문 표시를 하는 숫자를 +1씩 하면 목적지에 도달했을때
> (최단거리 + 1)이 목적지에 써짐 > 그래서 마지막 숫자 -1 이 최단거리  

강사님이 알려준 거리 측정법, len(queue)
> queue의 길이만큼만 반복
> 하나의 지점에서 근처에 갈 수 있는 지점을 발견하면 queue에 append함
> 그 길이를 측정해서 그 만큼만 반복하고 그 반복이 끝나면 depth(거리) +1
> -1할 필요없이 depth가 최단거리가 됨
'''

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

# 토마토 창고 받기
graph = [list(map(int, input().split())) for _ in range(N)]
# visited는 토마토 창고 만큼
visited = [[0] * M for _ in range(N)]

# 좌표들 담을 queue 생성
queue = deque([])

# graph 순회하면서 시작점 찾기
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            start_r = r
            start_c = c
            # queue에 시작점 좌표 추가
            queue.append((start_r, start_c))
            # 추가하고 방문체크
            visited[r][c] = 1

# 4방향 탐색 방향 설정
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# queue에 남아있을때까지 반복
while queue:
    # queue에 tuple로 넣었으니까 언패킹해서 x, y에 할당
    x, y = queue.popleft()

    # 4방향 탐색
    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        # graph 범위 내에 있다면
        if 0 <= nx < N and 0 <= ny < M:
            # 아직 안가봤고 0(익지 않은 토마토)이라면
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                # 탐색된 좌표의 visited는 현재 좌표의 visited의 + 1
                visited[nx][ny] = visited[x][y] + 1
                # 그리고 queue에 추가
                queue.append((nx, ny))

ans = 0
# graph와 visited를 순회하면서
for r in range(N):
    for c in range(M):
        # 두 개중 하나라도 0(방문하지 않은 곳이거나 익지 않은 토마토가 있다면)이라면
        if graph[r][c] == 0 and visited[r][c] == 0:
            # -1 출력 (문제 조건)
            print(-1)
            # 그리고 바로 프로그램 종료
            exit()
        
        # 정상적으로 모든 토마토가 다 익었다면
        # visited중 가장 큰 숫자를 ans에 할당
        # > 최단거리 찾기
        ans = max(ans, visited[r][c])

# 최단거리 = visited에서 가장 큰 숫자 - 1
# > visited가 시작부터 1에서 시작해서 -1 해야함
print(ans - 1)

'''
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

# 토마토 창고 받기
graph = [list(map(int, input().split())) for _ in range(N)]
# 방문 여부만 체크하기 위한 visited (0: 미방문, 1: 방문)
visited = [[0] * M for _ in range(N)]

# 좌표들 담을 queue 생성
queue = deque([])

# graph 순회하면서 시작점(익은 토마토) 찾기
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            # 시작점 좌표 추가 및 방문 체크
            queue.append((r, c))
            visited[r][c] = 1

# 4방향 탐색 방향 설정
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 경과된 날짜를 저장할 변수 (0일부터 시작)
depth = 0

# queue에 남아있을 때까지 반복
while queue:
    # 현재 큐의 길이(현재 날짜에 처리해야 할 토마토 개수)를 측정
    queue_size = len(queue)
    # 이번 레벨(하루)에서 새롭게 익게 만든 토마토가 있는지 확인하는 플래그
    ripened_new = False

    # 현재 레벨에 있는 토마토들만큼만 반복 실행
    for _ in range(queue_size):
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            
            # graph 범위 내에 있고
            if 0 <= nx < N and 0 <= ny < M:
                # 아직 안 가봤고 익지 않은 토마토(0)라면
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    # 방문 체크 후 큐에 추가
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    # 새롭게 토마토를 익혔으므로 True로 변경
                    ripened_new = True
    
    # 한 단계(하루)가 끝났을 때, 새롭게 익은 토마토가 있었다면 depth +1
    if ripened_new:
        depth += 1

# 모든 탐색이 끝난 후 안 익은 토마토가 있는지 확인
for r in range(N):
    for c in range(M):
        # 원래 안 익은 토마토(0)인데 끝까지 방문하지 못했다면
        if graph[r][c] == 0 and visited[r][c] == 0:
            print(-1)
            exit()

# 마지막에 -1을 할 필요 없이 계산된 days를 바로 출력
print(depth)
'''