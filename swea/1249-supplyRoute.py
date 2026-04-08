'''
Dijkstra 알고리즘 사용

Dijkstra는 우선순위 큐에서 특정 노드가 pop되는 순간 해당 노드까지의 최단 거리가 보장됨
> 목적지(N-1, N-1) 도달 시 즉시 리턴
'''

from heapq import heappop, heappush

def dijkstra():
    # 초기화
    # (누적 가중치, 행, 열) 정보를 담을 우선순위 큐 생성
    # 출발점(0, 0)의 가중치는 0이고, 나머지 모든 지점까지의 거리는 무한대로 설정
    pq = [(0, 0, 0)]
    dist_lst = [[float('inf')] * N for _ in range(N)]
    dist_lst[0, 0] = 0

    while pq:
        # 가중치가 가장 낮은 노드를 추출
        dist, node_r, node_c = heappop(pq)

        # 조기 종료
        # Dijkstra의 특성상 큐에서 뽑힌 노드는 이미 최단 거리가 확정된 상태임
        # > 따라서 목적지(N-1, N-1)가 뽑히는 순간, 그 값이 최종 최단 거리임
        if node_r == N-1 and node_c == N-1:
            return dist

        # 중복 탐색 방지
        # 큐에 들어있던 정보가 현재 기록된 최단 거리보다 크다면 무시함
        # > 큐에 push된 이후 다른 경로를 통해 더 짧은 거리가 이미 업데이트된 경우임
        if dist > dist_lst[node_r][node_c]:
            continue

        # 인접 노드(상하좌우) 탐색
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = node_r + dr, node_c + dc

            # 인덱스 범위 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 현재 노드를 거쳐서 다음 노드로 가는 새로운 가중치 계산
                new_dist = dist + area[nr][nc]

                # 새로 계산한 경로가 기존에 알고 있던 거리보다 짧을 때만 정보를 업데이트하고 큐에 삽입
                if new_dist < dist_lst[nr][nc]:
                    dist_lst[nr][nc] = new_dist
                    heappush(pq, (new_dist, nr, nc))

    return dist_lst[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 공백 없는 문자열이므로 strip() 후 한 글자씩 변환
    area = [list(map(int, input().strip())) for _ in range(N)]

    answer = dijkstra()
    print(f'#{tc} {answer}')