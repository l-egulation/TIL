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

T = int(input())

for tc in range(1, T+1):
    # 정점의 개수 V, 간선의 개수 E
    V, E = map(int, input().split())

    # 인접 리스트를 만듭니다. (노드 번호가 1번부터이므로 V+1 크기)
    # > 0번은 비우는 것
    graph = [[] for _ in range(V+1)]
    
    # 간선의 정보를 입력받아 그래프를 완성
    for i in range(1, E+1):
        u, v = map(int, input().split())
        # 일방향 u에서 v로 가는 길만 저장
        graph[u].append(v)

    # 출발 노드 S, 도착 노드 G
    S, G = map(int, input().split())
    
    # 작은 번호의 노드부터 방문하도록 정렬
    for i in range(1, V+1):
        graph[i].sort()
    
    # 각 테스트 케이스마다 방문 리스트와 결과값을 초기화
    visited = [False] * (V+1)
    result = 0

    # DFS 탐색
    dfs(S, G)
    
    print(f'#{tc} {result}')