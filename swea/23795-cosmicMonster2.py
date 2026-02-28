T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    '''
    괴물의 레이저 범위에 다 2로 만들기
    벽(0)에 만나면 멈추기
    '''

    # 상 하 좌 우
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    monster_lst = []
    # 괴물의 위치(시작점) 찾기
    for r in range(N):
        for c in range(N):
            if area[r][c] == 2:
                start_r = r
                start_c = c
                monster_lst.append((start_r, start_c))
    # monster_lst = [(a, b), (c, d)]

    for r, c in monster_lst:
        # 4방향으로 탐
        for i in range(4):
            # area끝까지 갈 수 있도록 for문으로 방향에 곱셈
            for j in range(N):
                nr = r + dr[i]*j
                nc = c + dc[i]*j

                # 만약 이동한 위치가 범위 내에 있고
                if 0 <= nr < N and 0 <= nc < N:
                    # 0이라면
                    if area[nr][nc] == 0:
                        # 2로 만들기
                        area[nr][nc] = 2
                    # 진행하다가 1(벽)을 만나면 중단
                    elif area[nr][nc] == 1:
                        break

    target = 0
    answer = sum(row.count(target) for row in area)
    print(f'#{tc} {answer}')