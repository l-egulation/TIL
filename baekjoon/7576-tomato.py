import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

for r in N:
    for c in M:
        if graph[r][c] == 1:
            start_r = r
            start_c = c

queue = deque([(start_r, start_c)])

while queue:
    n = queue.popleft()

    
'''
visited가 필요한가?
> graph가 있어서 그냥 0을 1로 만들면서 가면 될 것 같음

그럼 depth는 어떻게 확인?
> 이동할 때마다 depth +1?

dir 사용?

행 순회를 하는데, queue를 어떻게 써야할까?
> 그래서 원래는 노드 번호를 큐에 집어넣고 빼고 했는데 지금은 2차원 리스트(행렬)에서 앞옆뒤를 갈 수 있냐마냐를 확인해야됨
> 2차원 리스트의 전체를 다 간선으로 연결할 수는 없음
> 그래서 튜플 형태로 (r, c)를 집어넣어야 하나 싶음
'''
