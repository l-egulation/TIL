'''
일단 while문 사용해야 될 듯
> 언제 끝날지 몰라서

각 빙산에 대해서 델타로 0 개수 뽑기
while 한 번 반복이 1년으로 생각
> 한 번 반복할 때 마다 0개수 만큼 빙산에서 빼기
>> 빙산에서 0개수 만큼 뺐는데 음수로 떨어지면 0으로 취급하는 문장있어야함
> 한 번 반복할 때 years +1
뺀 후에 덩어리 체크
> 덩어리 count가 2이상이면 break하고 years 출력

로직 1. 빙산 주위의 0 개수 뽑기
> area 순회하면서 0이 아닌 수 위치 뽑기
> 각 위치마다 델타 돌려서 각 위치의 0개수 뽑기
>> 각 위치에서 0개수 뽑고, 그 개수만큼 바로 빼면 안되나?
>> while문 안에 바로 로직 집어넣으면 될 듯?
>> 대신 years 초기값을 1년으로 > 찾자마자 바로 빼버리니까

로직 2. 각 빙산에서 0 개수 빼기
> 로직 1이랑 합쳐서 pass

로직 3. 덩이리 체크하기
'단지번호붙이기'처럼 area 전체 순회해서 0아닌 수 찾고 bfs_count 돌림
> 빙산 수 count해서 추가해서 result 길이가 2면(덩어리가 2개면) while문 종료하고, years 출력

-------------------------------------------

회고록

문제점 1. 실시간 녹이기
> 빙산 좌표에서 근처 0 발견하자마자 빼버리니까 다른 빙산에 영향을 줘서 안녹을것도 녹아버림
> 어떤 빙산이 먼저 탐색되서 0이 되면, 바로 옆에 있는 빙산은 방금 녹은 빙산을 '원래 바다였던 곳'으로 인식
> 그래서 더 많이 녹게됨 > ㅂ신 빡대가리련
>> 각 빙산마다 녹을 양을 계산해서 리스트에 담고, 나중에 한꺼번에 녹임
>> 빙산 좌표 리스트를 각각 순회하는데, 빙산 좌표 리스트의 순서가 같음
>> 인덱스로 순회해서 녹을 양을 빼줌

문제점 2. 2중 for문 매번 반복
> while문 안에 NxM 2중 for문이 들어있어서 매우 무거움
>> 그래서 초기 빙산 좌표를 리스트에 저장하고 그 만큼만 순회
>> 후에 빙산을 녹이고 녹은 좌표(0이 된 좌표)는 빙산 좌표 리스트에서 제거
>> 정확히는 빙산 좌표 리스트를 새로 작성

기타 문제점
> visited랑 단지 개수 체크하는 리스트를 while문 밖에 빼놔서 무한루프 >> 진짜 개ㅂㅅ
> 빙산이 두 덩어리로 나눠지기전에 모두 녹아버리는 경우를 생각못함

'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 탐색을 위한 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_count(r, c):
    # BFS니까 큐에 시작 좌표 넣고 출발함
    queue = deque([(r, c)])
    # 시작점부터 방문체크
    # > 1을 찾고 bfs 시작이기 때문에 시작점도 포함
    visited[r][c] = True
    # 지금 찾은 빙산부터 카운트 1 시작함
    # > 위와 같은 이유
    count = 1

    while queue:
        # 현재 위치 꺼내서 주변 수색
        curr_r, curr_c = queue.popleft()

        # 4방향 탐색
        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if 0 <= nr < N and 0 <= nc < M:
                # 빙산이 있고 아직 안 가본 곳이면? 바로 이동
                if area[nr][nc] != 0 and not visited[nr][nc]:
                    # 방문 처리
                    visited[nr][nc] = True
                    # 다음 탐색 후보로 큐에 담음
                    queue.append((nr, nc))
                    # 빙산 개수 추가
                    count += 1

    # 총 빙산 개수 반환
    return count

icebergs = []

for i in range(1, N-1):
    for j in range(1, M-1):
        if area[i][j] != 0:
            icebergs.append((i, j))

years = 0

while True:
    visited = [[False]*M for _ in range(N)]

    # 단지별 빙산 개수 담을 리스트
    result = []

    # 덩어리 개수 확인
    for i, j in icebergs:
        if not visited[i][j]:
            # bfs 호출
            complex_count = bfs_count(i, j)
            result.append(complex_count)

    # 두 덩어리 이상으로 쪼개지면
    if len(result) >= 2:
        print(years)
        break
    # 쪼개지기 전에 다 녹아버렸다면
    if len(result) == 0:
        print(0)
        break

    # 빙산 녹을 양 계산
    melt_list = []
    for r, c in icebergs:
        zero_count = 0

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if area[nr][nc] == 0:
                zero_count += 1
        melt_list.append(zero_count)

    # 빙산 녹이기
    for k in range(len(icebergs)):
        r, c = icebergs[k]
        area[r][c] = max(0, area[r][c]-melt_list[k])

    # 녹은 빙산은 리스트에서 제거
    icebergs = [(r, c) for r, c in icebergs if area[r][c] > 0]

    years += 1