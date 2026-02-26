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

------------------------------------------------------------------------

처음엔 위처럼 생각함
근데 위의 논리로 접근하니까 반례가 너무 많이 생김

graph를 순회하면서 1이 나오면 bfs를 할 생각을 못했음
> for문 안에서 정의된 함수를 실행한다는 것을 생각을 못했다는 것

그래서 1을 카운트하는 bfs함수를 정의
> graph를 순회하면서 1을 만나면 bfs실행
> 연결되어있는 1을 모두 카운팅함
> 카운팅 할때마다 count +1을 하고 count를 return함
> return된 값을 result라는 리스트에 넣음
>> 단지 개수는 len(result)가 되고, for문으로 result를 순회하면서 값을 하나씩 출력
>> 단, 단지에 속하는 집의 수가 오름차순이므로 순회해서 출력하기 전에 sort한 후에 순회 및 출력
'''
import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우 탐색을 위한 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_count(r, c):
    # BFS니까 큐에 시작 좌표 넣고 출발함
    queue = deque([(r, c)])
    # 시작점부터 방문체크
    # > 1을 찾고 bfs 시작이기 때문에 시작점도 포함
    visited[r][c] = 1
    # 지금 찾은 집부터 카운트 1 시작함
    # > 위와 같은 이유
    count = 1

    while queue:
        # 현재 위치 꺼내서 주변 수색
        curr_r, curr_c = queue.popleft()
        
        # 4방향 탐색
        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            # 지도 밖으로 탈출 안 했는지 체크
            if 0 <= nr < N and 0 <= nc < N:
                # 집이 있고 아직 안 가본 곳이면? 바로 이동
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    # 방문 처리
                    visited[nr][nc] = True
                    # 다음 탐색 후보로 큐에 담음
                    queue.append((nr, nc))
                    # 집 개수 추가
                    count += 1
    
    # 총 집 개수 반환
    return count

# 입력 및 그래프 초기화 세팅
N = int(input())
# 지도 그리기
graph = [list(map(int, input().strip())) for _ in range(N)]
# 방문 기록장 초기화
visited = [[False]*N for _ in range(N)]

# 단지별 집 개수 담을 리스트
result = []

# 전체 지도 순회 시작
for i in range(N):
    for j in range(N):
        # 집 발견했는데 아직 안 가본 단지다?
        if graph[i][j] == 1 and not visited[i][j]:
            # bfs 호출
            complex_count = bfs_count(i, j)
            # 결과 리스트에 결과값 넣기
            result.append(complex_count)

# 오름차순 출력은 문제 조건이라 정렬 필수
result.sort()
# 총 단지가 몇 개인지 먼저 출력
print(len(result))
for answer in result:
    # 각 단지의 집 개수 하나씩 출력
    print(answer)