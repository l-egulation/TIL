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

'''
def find_set(x):
    if parent[x] == x:
        return x
    # 경로 압축(Path Compression): 찾는 김에 리더를 내 부모로 바로 연결 (성능 최적화)
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        # 두 팀의 리더가 다르면, 한쪽을 다른 쪽 밑으로 보냄
        parent[root_y] = root_x

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))

    parent = [i for i in range(N+1)]

    for i in range(0, len(temp), 2):
        leader = temp[i]
        member = temp[i+1]
        union(leader, member)

    answer = 0

    for i in range(1, len(parent)):
        if parent[i] == i:
            answer += 1

    print(f'#{tc} {answer}')