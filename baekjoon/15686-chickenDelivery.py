'''
'치킨 거리' 이름 너무 구림
차라리 치세권이 나을 듯
아닌가..?

근데 본사 ㅈㄴ 너무하네 가만히 장사하던 가맹점 폐업시켜버리면
그 사람들은 어캄?

일단 matrix 순회하면서 1(집)을 탐색 > 토마토로 따지면 시작점 찾는 것
그리고 각 집에서 2(치킨집)을 탐색
> 해당 1에서 2를 찾으면 '치킨 거리' 계산
> min(ans, graph[r][c]) 이거 써서 치킨 거리들 중 가장 작은 치킨 거리와 해당 2의 좌표만 저장
> 이게 살짝 문제인게 치킨거리 저장까지는 ok, 근데 그 좌표까지 저장하려니까 방법이 안보임
> 딕셔너리가 필요할 지도?
> 딕셔너리에 치킨거리를 key로 value에 해당 치킨 거리의 좌표 넣기
> 딕셔너리를 value를 기준으로 정렬하고 가장 작은 
> 그냥 복잡하게 하지말고 2를 찾으면 치킨거리 계산하고 지금 치킨거리가 전에 min으로 저장했던 값보다 작으면
현재 치킨거리를 min에 저장하고, 좌표도 저장 > 최솟값 나올때마다 계속 바꾸는 식

그래서 각 1(집)마다 min과 해당 2(치킨집)의 좌표가 나옴
이 중에서 최대 M개를 선택
> 최대 M개를 선택하는 기준이 중요

역으로 2를 시작점으로 해서 1을 찾아나가야 하나?

각 1마다 모든 2까지의 거리를 측정하고 가장 짧은 거리(min), 가장 먼 거리(max)의 2의 좌표를 저장
> 가장 짧은 거리가 많은 2의 순서대로 정렬 후 앞에서 부터 M개 선택

graph에서 선택한 2를 제외하고 재측정?
> 좀 비효율적인거 같은데
> 그냥 min, max 측정할때 더해서 측정하고 싶은데
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque([])

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            visited[r][c] = True
            queue.append((r, c))

while queue:
    x, y = queue.popleft()

    for next_node in graph:
        pass