'''
모든 노드를 연결하는 문제 > Prim 알고리즘 사용

여기서 가중치 weight = E * L**2 > L**2 = (x1-x2)**2 + (y1-y2)**2

양방향으로 모든 노드 연결
> 연결을 안하면 안되나?
> 어짜피 x, y 따로 좌표 다 있고, 선이 따로 정해진게 아니라서 연결해야 되나 싶음
>> 애초에 모든 노드에서 다른 모든 노드로 갈 수 있으니까 연결 X
>> 자기 자신 노드를 제외하고 visited 체크가 안된 모든 노드가 후보임

별도의 변수 생성 X
> 입력받은 x_lst와 y_lst의 인덱스(0 ~ N-1)를 각 노드의 고유 번호로 활용

가중치 구하는 것만 유클리드 거리로 하고 나머지는 prim 알고리즘이랑 동일

--------------------------------------------------

단순히 int()로 버림 처리를 했을 때 1 차이로 오답이 발생
> 'int(result + 0.5)' 사용

원래 count 없이 하니까 시간이 오래걸림
> count 사용해서 모든 정점이 연결되면 break
> 시간이 1/4로 감소
'''
from heapq import heappush, heappop

def prim():
    # (가중치, 노드 번호)
    # > 가중치를 실수형(0.0)으로 초기화하여 타입 일관성 유지
    pq = [(0.0, 0)]
    visited = [0] * N
    min_weight = 0.0
    count = 0  # MST에 포함된 정점의 개수를 추적

    while pq:
        # 가장 가중치가 낮은 간선을 선택
        weight, node = heappop(pq)

        # 이미 MST에 포함된 정점이라면 스킵 > Cycle 방지
        if visited[node]:
            continue

        # 정점을 MST에 포함시키고 방문 처리
        visited[node] = 1
        min_weight += weight
        count += 1

        # 모든 노드가 연결되었다면 조기 종료 > N-1개의 간선이 선택된 시점
        if count == N:
            break

        # 현재 정점에서 갈 수 있는 다른 모든 정점 탐색
        for i in range(N):
            if not visited[i]:
                # 문제의 가중치 공식: E * L^2
                # L^2 = (x1-x2)^2 + (y1-y2)^2 > 유클리드 거리의 제곱
                dist = (x_lst[node] - x_lst[i])**2 + (y_lst[node] - y_lst[i])**2

                # 인접 리스트를 따로 만들지 않고, 매번 계산하여 힙에 삽입
                heappush(pq, (dist, i))

    return min_weight

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # x, y 좌표 리스트를 인덱스로 관리하여 노드 번호로 사용
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())

    # 결과값은 소수점 첫째 자리에서 반올림 > 1 차이나서 틀리는 거 방지
    answer = int(E * prim() + 0.5)

    print(f'#{tc} {answer}')