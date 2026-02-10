def dfs(start, end):
    # 전역 변수 result를 global로 가져옴
    # > 테스트 for문 안이 아니라 밖에 있으면 0으로 초기화가 안됨
    global result
    
    # 현재 방문한 노드(start)를 방문 처리
    visited[start] = True

    # 현재 위치가 목표 지점(end)과 같다면 성공
    if start == end:
        # 결과값을 1로 변경
        result = 1
        # 현재 함수를 종료하고 이전 단계로 복귀
        return

    # 현재 노드와 연결된 다음 노드들을 하나씩 확인
    for next_node in graph[start]:
        # 만약 다음 노드를 아직 방문하지 않았다면 탐색
        if not visited[next_node]:
            # 다음 노드를 시작점으로 하여 다시 dfs를 호출
            dfs(next_node, end)
            
            # 재귀를 타고 들어갔다가 나왔을 때, 이미 목표를 찾았다면
            if result == 1:
                # 더 이상 다른 경로를 찾지 않고 즉시 함수를 종료
                return

for tc in range(1, 11):
    # 테스트 케이스 번호 _, 간선의 개수 M
    _, M = map(int, input().split())

    # 0번부터 99번까지의 노드를 담기 위해 100개의 빈 리스트를 만듦
    # > 인접 리스트 방식
    graph = [[] for _ in range(100)]
    
    # 한 줄로 들어오는 모든 간선 정보를 리스트로 받음
    link_lst = list(map(int, input().split()))

    # 리스트에서 두 개씩 짝을 지어 간선 정보를 그래프에 넣음
    # > 두 개씩 짝이므로 step = 2
    for i in range(0, M*2, 2):
        u, v = link_lst[i], link_lst[i+1]
        # 일방향 u에서 v로 가는 길만 저장
        graph[u].append(v)

    # 문제에서 정해준 시작점 S는 0, 도착점 G는 99
    S, G = 0, 99
    
    # 탐색 순서를 일정하게 맞추기 위해 각 노드의 인접 리스트를 정렬
    for i in range(100):
        graph[i].sort()
    
    # 각 테스트 케이스마다 방문 리스트와 결과값을 초기화
    visited = [False] * (100)
    result = 0

    # DFS 탐색
    dfs(S, G)
    
    print(f'#{tc} {result}')