import sys

# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    # 2. V(정점의 개수), E(간선의 개수)를 읽습니다.
    line = input().split()
    if not line: break  # 입력이 예상보다 적을 경우를 대비한 안전장치
    V, E = map(int, line)

    # 3. 인접 리스트 방식의 그래프 생성
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)

    # 4. 출발 노드 S와 도착 노드 G를 읽습니다.
    S, G = map(int, input().split())

    # 5. DFS에 필요한 도구들 준비
    stack = [S]              # 방문할 곳을 담는 스택
    visited = [False] * (V + 1) # 방문 여부 체크 리스트
    result = 0               # 성공 여부 (기본값 0)

    # 6. 반복문을 이용한 DFS 탐색
    while stack:
        curr = stack.pop() # 가장 나중에 들어온 놈을 꺼냅니다 (LIFO)

        # 목표 지점에 도달했는지 확인
        if curr == G:
            result = 1
            break

        # 아직 방문하지 않은 노드라면 탐색 진행
        if not visited[curr]:
            visited[curr] = True # 방문 도장 쾅!
            
            # [중요] 작은 번호부터 방문하기 위해 '역순'으로 스택에 넣습니다.
            # 그래야 pop() 했을 때 작은 번호가 먼저 튀어나와요.
            for next_node in sorted(graph[curr], reverse=True):
                if not visited[next_node]:
                    stack.append(next_node)

    # 7. 문제 양식에 맞춰 결과 출력
    print(f'#{tc} {result}')