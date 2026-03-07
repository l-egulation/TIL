'''
1. 1(시작점)을 찾는다.
    > 1을 찾는 것
    > 원래 가장자리에 위치한 1, 4방향 모두에 0이 아닌 수가 있으면 제외하려고 했음
    > 가장자리에 위치한 1을 제외하는 건, for문의 범위를 줄여서 간단함
    > 근데 4방향 모두 0이 아닌 수가 있으면 제외처리하는게 너무 많은 for문을 돌아야함
    > 이걸 가능하게 하면 반드시 연결해야할 1의 개수를 알 수 있어서 편하긴 함

2. 시작점을 기준으로 가장자리까지 한 방향으로만 2(전선)를 채운다.
    > 단 하나의 1에서만 전선을 연결하는 것

3. 전선 연결이 가능한 모든 경우의 수를 시도한다.
    > 재귀를 사용해야된다고 생각함
    > 방향에다가 visited를 체크해야하나?
    > 그래야 갔던 방향이 아니라 다른 방향을 가나..?

시작점은 하나씩 다 써야됨
> 그래서 시작점을 가지고 조합, 순열 따질 필요가 없음

델타의 4방향, dir을 중복순열로 해야함
> for dir in range(4): 해서 dir을 중복순열로 뽑아서 하나씩 나가야함
>> Up, Right, Down, Left == [0, 1, 2, 3]
>> 그래서 좌표가 5개면 00000, 00001, 00002, ... , 00201
>> 이런식으로 순차적으로 다 돌기

근데 이제 core가 연결이 안된 경우도 있을 수도 있음
그래서 최대로 연결 가능한 코어 수를 저장해두고, 그 코어 수에 못 미치면 그 경우의 수에서 나온 wire수는 폐기

그래서 for start in start_lst: 해서 시작점 순회하면서 dir을 중복순열로 뽑아서 여러 경우의 수 해보기

-----------------------------------------------------

[문제 요약]
- N x N 그리드에서 가장자리를 제외한 코어(1)들을 최소한의 전선(2)으로 최대한 많이 연결하기.
- 1순위: 최대한 많은 코어 연결 / 2순위: 전선 길이의 합 최소화.

--------------------------------------------------

# 1. 핵심 설계 포인트 (Key Realizations)

(1) 탐색의 구조 (중복 순열에서 DFS/백트래킹으로):
    - 초기 생각: 4방향을 중복 순열(00000~33333)로 뽑아 모든 코어를 연결하려 함.
    - 발전: 코어당 [상, 하, 좌, 우, 연결 안 함]의 5가지 선택지를 가진 DFS로 전환.
    - 이유: 모든 코어를 억지로 연결하려 하면 전선이 꼬여 아예 해를 못 찾을 수 있음.
        > '연결 포기'라는 선택지를 넣음으로써 다른 코어들을 위한 길을 열어주는 유연한 탐색이 가능해짐.

(2) 효율적인 전처리 및 가지치기:
    - 가장자리 코어 제외는 물론, 사방이 막혀 연결 불가능한 코어를 미리 제거하여 탐색 깊이를 줄임.
    - "남은 코어를 다 연결해도 현재 최고 기록을 갱신할 수 없다면 중단"하는 가지치기를 통해
        > 탐색 시간을 획기적으로 단축함.

(3) 상태 복구의 최적화:
    - 초기 생각: 배열의 복사본(Deepcopy/Backup)을 만들어 백트래킹을 구현하려 함.
    - 발전: 전선을 놓은 길만 다시 '0'으로 지워주는(Clear) 방식 선택.
    - 이유: N=12일 때, 매번 배열을 복사하는 오버헤드를 줄여 메모리와 실행 속도를 최적화함.

--------------------------------------------------

# 2. 셀프 피드백 (Self-Feedback)

- 초기 로직의 한계와 해결:
    처음에는 "모든 코어를 순회하며 방향을 정한다"는 중복 순열 방식에 집중했음.
    하지만 이 방식은 '연결이 불가능한 코어'가 하나라도 생기면 전체 탐색이 막히거나
    결과가 나오지 않는(0이 나오는) 문제가 있었음.
    이를 해결하기 위해 '연결하지 않고 건너뛰기'라는 선택지를 DFS의 한 갈래로 포함시킨 것이
    로직의 가장 큰 전환점이었음.

- 구현 상의 변화:
    방향에 대한 'visited' 체크를 고민했으나, 2차원 배열 자체가 전선(2)과 코어(1)라는
    방해물 정보를 가지고 있으므로 별도의 체크 배열 없이 지도 자체를 활용하는 것이
    더 효율적임을 깨달음.

- 결론:
    완전 탐색 문제에서 "아무것도 하지 않는 선택지"가 때로는 가장 중요한 해결 열쇠가
    될 수 있다는 점을 배움. 또한, 무작정 모든 경우를 다 보는 것이 아니라
    수학적으로 '가망 없는 길'을 미리 계산해 쳐내는(가지치기) 테크닉의 중요성을 실감함.
'''

# core(1)의 전원을 연결하는 함수
# 모든 코어에 대해서 하나씩 전선 다 연결하는 함수
# def connect_wire(location, dir):
#     global curr_core_count, curr_wire_count, visited_dir
#     r, c = location

#     for k in range(1, N):
#         nr, nc = r + dr[dir]*k, c + dc[dir]*k

#         if 0 <= nr < N and 0 <= nc < N:
#             if area[nr][nc] != 0:
#                 break
#             elif area[nr][nc] == 0:
#                 # 상
#                 # > 위로갔으니 다시 아래로
#                 if nr == 0 and not visited_dir:
#                     for i in range(k):
#                         area[i][nc] = 2
#                     curr_core_count += 1
#                     curr_wire_count += k
#                     return
#                 # 우
#                 # > 오른쪽으로 갔으니 다시 왼쪽으로
#                 elif nc == N-1 and not visited_dir:
#                     for i in range(N-1, N-1-k, -1):
#                         area[nr][i] == 2
#                     curr_core_count += 1
#                     curr_wire_count += k
#                     return
#                 # 하
#                 # > 아래로갔으니 다시 위로
#                 elif nr == N-1 and not visited_dir:
#                     for i in range(N-1, N-1-k, -1):
#                         area[i][nc] = 2
#                     curr_core_count += 1
#                     curr_wire_count += k
#                     return
#                 # 좌
#                 # 왼쪽으로 갔으니 다시 오른쪽으로
#                 elif nc == 0 and not visited_dir:
#                     for i in range(k):
#                         area[nr][i] = 2
#                     curr_core_count += 1
#                     curr_wire_count += k
#                     return

def fill_wire(idx, dir, num):
    r, c = start_lst[idx] # 현재 탐색 중인 코어의 좌표를 가져옴
    count = 0 # 새로 깔린 전선의 길이를 셀 변수

    nr, nc = r, c
    while True:
        nr += dr[dir] # 해당 방향으로 한 칸 이동
        nc += dc[dir]

        # 경계를 벗어나면 전선 설치 완료
        if not (0 <= nr < N and 0 <= nc < N):
            break

        area[nr][nc] = num # 전선 설치(2) 또는 제거(0)
        count += 1 # 전선 길이 증가
    return count # 총 설치된 전선 길이를 반환 (wire_count 누적용)

def is_connect(idx, dir):
    r, c = start_lst[idx]
    nr, nc = r, c

    while True:
        nr += dr[dir]
        nc += dc[dir]

        # 장애물 없이 경계에 도달하면 연결 가능
        if not (0 <= nr < N and 0 <= nc < N):
            return True

        # 가는 길에 0이 아닌 것(코어 1 또는 전선 2)을 만나면 연결 불가
        if area[nr][nc] != 0:
            return False

def dfs(idx, curr_core_count, curr_wire_count):
    global total_core_count, total_wire_count

    # [가지치기] 남은 코어를 다 연결해도 현재 기록(최대 연결 수)을 못 깨면 가차 없이 종료
    if (len(start_lst) - idx) + curr_core_count < total_core_count:
        return

    # [기저 조건] 모든 코어를 다 확인했을 때
    if idx == len(start_lst):
        # 1순위: 코어를 더 많이 연결했는가?
        if curr_core_count > total_core_count:
            total_core_count = curr_core_count
            total_wire_count = curr_wire_count
        # 2순위: 코어 수는 같은데 전선이 더 짧은가?
        elif curr_core_count == total_core_count:
            total_wire_count = min(total_wire_count, curr_wire_count)
        return

    # [경우의 수 1~4] 4방향으로 전선을 뻗어보는 경우
    for dir in range(4):
        if is_connect(idx, dir): # 연결 가능하면
            length = fill_wire(idx, dir, 2) # 전선 깔기 (2로 표시)
            dfs(idx + 1, curr_core_count + 1, curr_wire_count + length) # 다음 코어로 진행
            fill_wire(idx, dir, 0) # (중요) 다음 탐색을 위해 전선 다시 지우기 (복구)

    # [경우의 수 5] 현재 코어를 연결하지 않고 그냥 건너뛰는 경우
    dfs(idx + 1, curr_core_count, curr_wire_count)

# 상, 우, 하, 좌 방향 벡터
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    total_core_count = float('-inf')
    total_wire_count = float('inf')

    start_lst = []
    # 가장자리(r, c가 0이거나 N-1인 곳)를 제외하고 내부 코어만 탐색
    for r in range(1, N-1):
        for c in range(1, N-1):
            if area[r][c] == 1:
                can_connect = False
                # 이 코어가 4방향 중 단 한 곳이라도 뚫려 있는지 미리 체크
                for i in range(4):
                    nr, nc = r, c
                    while True:
                        nr += dr[i]
                        nc += dc[i]
                        if not (0 <= nr < N and 0 <= nc < N): # 경계 도착 성공
                            can_connect = True
                            break
                        if area[nr][nc] == 1: # 코어에 막힘
                            break
                    if can_connect: break

                # 최소 한 방향이라도 전선을 뺄 가능성이 있는 코어만 리스트에 추가
                if can_connect:
                    start_lst.append((r, c))

    # 0번 인덱스 코어부터, 연결 성공 0개, 전선 길이 0인 상태로 시작
    dfs(0, 0, 0)

    print(f'#{tc} {total_wire_count}')