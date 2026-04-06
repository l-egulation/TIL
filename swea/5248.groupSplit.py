'''
그룹 나누기
N : 1번부터 N번까지 있음
M : 신청서 제출한 횟수

input이 좀 헷갈렸음
1 2 3 4 이렇게 있으면 M이 2니까 신청서 2장
즉, 1 -> 2 / 3 -> 4 라는 뜻

저 입력을 받으면서 그룹을 생성, 그 후 visited 같은걸로 몇 번이 이미 조가 있는지 체크한다고 해야되나?
그래서 그룹을 이뤘으면 1, 아니면 0
answer = 그룹 수 + visited에서 0의 수 = group_num + visited.count(0)

문제는 저 input으로 어케 그룹 수를 체크하냐는 것
> find_set이랑 union
'''
def find_set(x):
    # 인덱스와 값이 일치하면 해당 노드는 트리의 루트(Root)임
    if parent[x] == x:
        return x

    # 루트 노드를 찾을 때까지 재귀적으로 부모 노드를 탐색함.
    # 탐색 과정에서 거쳐가는 모든 노드의 부모를 루트로 직접 업데이트하여
    # 트리의 높이를 상수로 만드는 '경로 압축'을 수행함.
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    # 각 원소가 속한 집합의 대표 원소(Root)를 추출함
    root_x = find_set(x)
    root_y = find_set(y)

    # 서로 다른 집합에 속해 있다면, 한쪽 루트의 부모를 다른 쪽 루트로 설정하여
    # 두 개의 분리된 트리를 하나의 트리로 병합함
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 짝수 인덱스는 출발 노드, 홀수 인덱스는 도착 노드로 간주되는 간선 정보 리스트
    temp = list(map(int, input().split()))

    # 1. 모든 노드가 자신을 부모로 갖는 독립적인 집합으로 설정 > Make-Set
    parent = [i for i in range(N+1)]

    # 2. 입력된 간선 정보를 바탕으로 합집합 연산 수행 > Union
    for i in range(0, len(temp), 2):
        u = temp[i]
        v = temp[i+1]
        union(u, v)

    answer = 0

    # 3. 전체 노드 중 루트 노드의 개수를 카운트
    # 분리 집합 포레스트에서 루트 노드의 개수는 서로소 집합의 개수와 동일함
    for i in range(1, len(parent)):
        if parent[i] == i:
            answer += 1

    print(f'#{tc} {answer}')