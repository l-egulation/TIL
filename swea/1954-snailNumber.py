T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail_lst = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = c = 0
    dir = 0

    for num in range(1, N*N+1):
        snail_lst[r][c] = num

        now_r = r + dr[dir]
        now_c = c + dc[dir]

        if now_r < 0 or now_r >= N or now_c < 0 or now_c >= N or snail_lst[now_r][now_c] != 0:
            dir = (dir+1) % 4
            now_r = r + dr[dir]
            now_c = c + dc[dir]

        r, c = now_r, now_c

    print(f'#{tc}')

    for snail in snail_lst:
        print(*snail)