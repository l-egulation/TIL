T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail_lst = [[0] * N for _ in range(N)]
    
    num_lst = []
    for num in range(1, N*N+1):
        num_lst.append(num)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    snail_lst[0][0] = num_lst[0]

    r = c = 0

    dir_num = 0

    for time in range(1, N*N-1):
        dir = dir_num % 4

        now_r = r + dr[dir]
        now_c = c + dc[dir]

        if 0 <= now_r < N and 0 <= now_c < N and snail_lst[now_r][now_c] != 0:
            continue
        else:
            dir_num += 1
        
        snail_lst[now_r][now_c] = num_lst[time]
    
    print(f'#{tc} {snail_lst}')