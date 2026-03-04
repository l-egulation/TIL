'''
선형 탐색으로 체크하면 됨
위치에 따라 충전소의 위치가 달라짐

dr, dc > 방향 이동
T > TC 수
M > 이동 횟수
N > 배터리의 수
A, B > 각각 A/B 이동 경로 (델타의 인덱스)
human_rcs > A(0), B(1) 좌표
BC_info > 배터리의 정보(N개)
charge_idxs > (0)A가 충전할 수 있는 위치 인덱스 모음, (1)B가 충전할 수 있는 위치 인덱스 모음

1. 이동 > M번
2. 이동한 위치에서 A와 B가 충전할 수 있는 충전소를 파악
    - A, B ~ 충전소의 거리를 파악 > 해당 거리가 충전 범위 이내이면 충전 가능
3. 최적의 충전량을 고르기 > 각각의 위치에서의 max값
    a. A만 충전할 수 없는 경우 > B를 반복
    b. B만 충전할 수 있는 경우 > A를 반복
    c. A, B 둘 다 충전 가능한 경우
4. max 누적
'''

# 1: 상, 2: 우, 3: 하, 4: 좌
# > 문제에서 r, c가 바뀌어 있어서 반대로 바꿈
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]

T = int(input())

for tc in range(1, T+1):
    # 충전량이 없을 수도 있어서 초기값 0으로 세팅
    answer = 0

    # M : 이동 횟수
    # N : 배터리의 수
    M, N = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 위치가 바뀌기 때문에 튜플이 아닌 리스트로 설정
    # 시작 위치가 각각 정해져있기 때문에 초기값 고정
    human_rcs = [[1, 1], [10, 10]]

    # BC_info > N
    # 0, 1 > 좌표
    # 2 > 충전 범위
    # 3 > 충전량
    BC_info = [0]*N
    for i in range(N):
        BC_info[i] = list(map(int, input().split()))

    # 이동
    # 충전 > M+1 > 초기 위치에서부터 충전이 가능해서 M+1
    for time in range(M+1):
        # 충전을 하고 이동
        # 충전 가능한 위치를 탐색 > 최적 충전량을 충전 > 이동
        # 충전 가능한 위치 탐색 - A, B
        charge_idxs = [[], []]
        # A, B 중 누구를 돌지 > 0 / 1
        # i : A인지 B인지 > 사람 번호
        for i in range(2):
            r, c = human_rcs[i]
            # 어떤 충전소인지 선택
            # j : 충전소 번호
            for j in range(N):
                BC_r, BC_c, coverage, charge_amount = BC_info[j]

                if abs(r-BC_r) + abs(c-BC_c) <= coverage:
                    charge_idxs[i].append(j)

        # 최적 충전량 - a, b, c
        charge = 0
        # a. A가 충전할 수 없는 경우
        if not charge_idxs[0]:
            for i in charge_idxs[1]:
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]

        # b. B가 충전할 수 없는 경우
        elif not charge_idxs[1]:
            for i in charge_idxs[0]:
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]

        # c. A와 B 모두 충전 가능한 경우
        else:
            # i : A의 충전소 번호
            for i in charge_idxs[0]:
                # j : B의 충전소 번호
                for j in charge_idxs[1]:
                    if i == j:
                        if BC_info[i][3] > charge:
                            charge = BC_info[i][3]
                    else:
                        if BC_info[i][3] + BC_info[j][3] > charge:
                            charge = BC_info[i][3] + BC_info[j][3]

        answer += charge

        # 이동
        if time == M:
            break

        human_rcs[0][0] += dr[A[time]]
        human_rcs[0][1] += dc[A[time]]

        human_rcs[1][0] += dr[B[time]]
        human_rcs[1][1] += dc[B[time]]

    print(f'#{tc} {answer}')