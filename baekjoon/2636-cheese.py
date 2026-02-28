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

#회고록#

# STEP 1. 초기 접근: "내부의 적(갇힌 공기)을 찾아라" (실패)

- 생각: "치즈 안에 갇힌 구멍(0)을 찾아서, 얘네랑 닿은 치즈는 안 녹게 보호해야지!"

- 한계: '갇혀 있다'는 것을 정의하기가 너무 복잡함. (모든 0 덩어리를 BFS로 돌며 가장자리와 닿았는지 체크해야 함)

- 교훈: 복잡한 제외 대상을 찾는 것보다, 확실한 작용 대상을 찾는 게 훨씬 쉽다.

# STEP 2. 발상의 전환: "외부 공기의 역습" (성공)

- 전략: "가장자리 (0,0)은 무조건 외부 공기다! 여기서부터 BFS를 돌려 뻗어나가며 만나는 공기들이 진짜 '치즈를 녹이는 공기'다."

- 결과: (0,0) 출발 BFS 한 번으로 '녹일 수 있는 공기'와 '갇힌 공기'가 자동으로 분류됨. (방문 못한 0은 갇힌 공기)

# STEP 3. 데이터 구조 최적화: external_air (set)의 삭제

- 기존: BFS로 찾은 외부 공기 좌표들을 set에 담아 보관함.

- 변경: 어차피 BFS를 돌면 visited 배열이 만들어지는데, visited[r][c] == True인 곳이 곧 외부 공기임.

- 이유: set에 넣고(add) 찾는(in) 해시 연산보다, 배열 인덱스(visited[r][c])로 직접 접근하는 것이 메모리와 속도 면에서 압승.

# STEP 4. 알고리즘 최적화: "원샷원킬" (최종 진화)

- 기존 (2단계 전략):

1. 외부 공기 마킹 BFS 수행.

2. cheese_lst를 순회하며 사방에 외부 공기가 있는지 다시 확인. (이중 작업)

- 변경 (현재 코드):

- 외부 공기 BFS를 돌다가 치즈(1)를 만나는 즉시 melt_lst에 담기.

- 이유 (효율성):

1. 별도의 치즈 리스트 순회 로직을 삭제하여 연산 횟수를 획기적으로 줄임.

2. 치즈를 발견하면 visited 처리만 하고 큐(queue)에는 넣지 않음으로써, 치즈 안쪽으로 탐색이 들어가는 것을 자연스럽게 방어함.

'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

def bfs_external_air(melt_lst):
    # 매 시간마다 방문 지도를 새로 만듦
    visited = [[False]*M for _ in range(N)]

    # 항상 가장자리인 (0,0)에서 공기 탐색을 시작
    queue = deque([(0, 0)])

    # 시작점 방문 표시
    visited[0][0] = True
    # ! external_air = set()
    # ! external_air.add((0, 0))

    while queue:
        # 현재 위치 꺼냄
        r, c = queue.popleft()

        # 4방향 탐색
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            # 지도를 벗어나지 않고, 아직 확인하지 않은 좌표라면?
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # [공기를 만난 경우]
                if area[nr][nc] == 0:
                    # 방문 표시를 하고
                    visited[nr][nc] = True
                    # 이 공기를 타고 더 멀리 뻗어나갑니다.
                    queue.append((nr, nc))
                    # ! external_air.add((nr, nc))
                # [치즈를 만난 경우] - '원샷' 최적화 포인트
                elif area[nr][nc] == 1:
                    # 중복으로 담기지 않게 방문 표시만 하고
                    visited[nr][nc] = True
                    # 큐에 넣지 않고 '녹을 명단'에 바로 추가
                    melt_lst.append((nr, nc))
                    # 💡 치즈를 큐에 넣지 않으므로, 공기는 치즈 내부 구멍으로 파고들지 못함

# 녹는 데 걸린 시간
hours = 0
# 다 녹기 직전의 치즈 개수 보관용
last_cheese_count = 0

# 현재 치즈들의 좌표를 보관
cheese_lst = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            cheese_lst.append((i, j))

while True:
    # 1. 종료 조건 확인: 남은 치즈가 없으면 멈춤
    if not cheese_lst:
        break

    # 2. 이번 시간에 녹기 전 치즈 개수를 백업
    # 이 값이 결국 "다 녹기 한 시간 전 개수"
    last_cheese_count = len(cheese_lst)

    # 이번 루프(1시간)에서 녹을 치즈들을 담을 바구니
    melt_lst = []
    # 외부 공기 탐색을 통해 melt_lst를 채움
    bfs_external_air(melt_lst)


    # ! melt_lst = []
    # ! for r, c in cheese_lst:
    # !     for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    # !         if external_air[r+dr][c+dc]:
    # !             melt_lst.append((r, c))
    # !             break

    # 3. 선별된 치즈들을 실제로 녹임 (1 -> 0)
    for mr, mc in melt_lst:
        area[mr][mc] = 0

    # 4. 살아남은 치즈들만 골라내어 cheese_lst를 갱신
    # 리스트 컴프리헨션을 사용하여 효율적으로 필터링
    cheese_lst = [(r, c) for r, c in cheese_lst if area[r][c] == 1]

    # 1시간 경과
    hours += 1

# 치즈가 모두 녹는 데 걸린 총 시간
print(hours)
# 모두 녹기 1시간 전의 치즈 개수
print(last_cheese_count)