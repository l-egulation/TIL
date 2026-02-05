T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, list(str(input()))))

    k = max(num_lst)
    counts = [0] * (k+1)

    for i in range(N):
        counts[num_lst[i]] += 1

    max_cnt = 0
    max_num = 0

    for i in range(len(counts)):
        if counts[i] >= max_cnt:
            max_cnt = counts[i]
            max_num = i
    
    print(f'#{tc} {max_num} {max_cnt}')