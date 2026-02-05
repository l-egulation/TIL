T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_lst = list(map(int, input().split()))

    count = [0] * (N+1)

    for num in M_lst:
        count[num] = 1
    
    now_idx = 0
    charge_cnt = 0

    while (now_idx + K) < N:
        for i in range(now_idx + K, now_idx, -1):
            if count[i] == 1:
                now_idx = i
                charge_cnt += 1
                break
        else:
            charge_cnt = 0
            break

    print(f'#{tc} {charge_cnt}')