T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail_lst = [[0] * N for _ in range(N)]

    '''
    N by N 일 때, 행렬 순회 바뀔 때마다 바뀐 횟수 +=1 로 저장하고,
    일정 규칙의 횟수가 되면 N-1, N-2, ... 이런 식으로 회전 주기?개수?를 짧게하기
    그 규칙 찾기'
    N - num == 1이면 break
    왜냐면 1이 되면 마지막 수라서.
    3 5
    4 7
    => N*2-1 만큼 회전하는 듯?

    델타쓰면 쉽긴할 듯
    델타로 돌면서 배열하기(할당?)

    회전하면서 할당하는데 회전이 N회차가 되면 회전 횟수 N-1
    => 약간 0은 비어있다고 생각하면 돌다가 벽에 부딪히면 돌기
    => 돌다가 0이 아니면 벽이라고 생각가하고 다시 돌기 (시계방향으로)
    '''
    num_lst = []
    for num in range(1, N*N+1):
        num_lst.append(num)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # dr, dc를 같은 인덱스끼리 한 쌍으로 봤을 때, 0번부터 차례대로 우, 하, 좌, 상

    now_r = 0
    now_c = 0
    snail_lst[now_r][now_c] = num_lst[0]

    for r in range(N-1):
        for c in range(N-1):
            for d in range(4):
                while True:
                    now_r = r + dr[d]
                    now_c = c + dc[d]
                    
                    if 0 <= now_c < N and 0 <= now_r < N: # and 다음 할당 위치의 값이 0이라면 할당
                        pass # 옮겨가면서 각 위치에 값 할당하기

    
    # dir => 0 > 1 > 2 > 3 > 0
    # dir = (dir+1) % 4  -> 방향 바꿀땐 이걸 쓰면 될 듯
    # for 반복횟수 = N*N
        # 숫자 적기(생각해보기)
        # 1. 현재 좌표(r, c)로부터 정해진 방향(dir)으로 이동
        
        # 2. 정해진 방향으로 이동하지 못하는 경우엔 방향 전환 후 이동
        # r+dr[dir] c+dc[dir] > 맵이 넘어가진 않는지, 해당 좌표에 이미 숫자가 적혀있는지
        # 위 경우가 아니라면 방향 전환
    
    '''
    snail_lst[0][0] = num_lst[0]

    now_r = 0
    now_c = 0

    dir_num = 0

    for time in range(1, N*N-1):
        dir = dir_num % 4

        now_r = r + dr[dir]
        now_c = c + dc[dir]

        => 이거 dir로 묶어서 해야되나 싶음
        => 왜냐면 dir=0 (우로 이동)을 여러번 해야되는데 for문을 한 번 돌면(1 -> 2) 우로 2번이 아니라
        => 우 -> 하 로 이동이 되버림.
        => 그럼 그냥 뺑글뺑글 도는거
        => 그럼 dir이 변하는 조건을 이동 조건문 아래로 내려서
        => 이동이 가능하면 기존 dir 유지, 아니라면 dir += 1

        //정해진 방향으로 이동하지 못하는 경우에 대한 조건문//
        if 0 <= now_r, now_c < N and snail_lst[now_r][now_c] != 0:
            continue
        else:  (더이상 이동 불가하다)
            dir_num += 1
        
        snail_lst[now_r][now_c] = num_lst[time]
    
    print(f'#{tc} {snail_lst}')
    '''