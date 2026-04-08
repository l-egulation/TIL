"""
heappop() 대체
> 'min_dist' 배열에서 방문하지 않은 노드 중 최솟값을 직접 선형 탐색
heappush() 대체
> 새 노드가 추가될 때마다 해당 노드에서 다른 노드들로의 거리를 계산
> 'min_dist' 배열의 값을 최신화

E * (L1^2 + L2^2 + ...) = E * Σ(L^2) 이므로 E 곱셈은 최종 결과에 한 번만 수행
"""

def prim():
    # 초기화
    # 각 노드가 MST에 합류하기 위해 필요한 최소 비용(거리 제곱) 저장
    inf = float('inf')
    min_dist = [inf] * N # 현재까지 알려진 각 노드로의 최소 거리 후보들
    visited = [0] * N    # 이미 MST에 포함된 노드인지 체크

    # 시작점 설정
    # 0번 섬부터 출발 > 어느 섬에서 시작해도 MST 결과는 동일함
    min_dist[0] = 0
    total_dist = 0    # 최종적으로 합산할 거리 제곱들의 합

    # 총 N개의 섬을 하나씩 MST로 끌어옴
    for _ in range(N):
        # 다음 후보 선정 > heappop 역할
        # 아직 MST가 아닌 섬들 중, 현재 노드와 가장 가까운 섬을 직접 찾음
        curr_node = -1
        min_val = inf

        for i in range(N):
            # 방문하지 않았고, 현재 알고 있는 거리 중 가장 짧은 노드 선택
            if not visited[i] and min_dist[i] < min_val:
                min_val = min_dist[i]
                curr_node = i

        # 더 이상 연결할 수 있는 노드가 없다면(모두 방문했거나 고립된 경우) 종료
        if curr_node == -1:
            break

        # MST 합류
        # 찾은 최솟값(min_val)을 결과에 더하고, 해당 노드를 방문 처리함
        visited[curr_node] = 1
        total_dist += min_val

        # 정보 업데이트 > heappush 역할
        # 방금 추가한 curr_node 덕분에 다른 섬들로 가는 지름길이 생겼는지 확인
        cx, cy = x_lst[curr_node], y_lst[curr_node]
        for i in range(N):
            if not visited[i]:
                # curr_node에서 i번 섬까지의 거리 제곱 계산
                dx = cx - x_lst[i]
                dy = cy - y_lst[i]
                d_sq = dx*dx + dy*dy

                # 만약 기존에 알고 있던 거리보다 curr_node를 거쳐서 가는 게 더 가깝다면 갱신
                # 다음 번 루프에서 이 갱신된 값이 최솟값 후보가 됨
                if min_dist[i] > d_sq:
                    min_dist[i] = d_sq

    return total_dist

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())

    # 가중치 합산 후 환경 부담 세율(E)을 곱하고 반올림 처리
    # sum(E * L^2) = E * sum(L^2) 원리 이용
    result = prim() * E
    answer = int(result + 0.5)

    print(f'#{tc} {answer}')