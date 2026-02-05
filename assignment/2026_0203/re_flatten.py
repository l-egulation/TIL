for tc in range(1, 11):
    dunp_num = int(input())
    origin_lst = list(map(int, input().split()))

    box_lst = sorted(origin_lst)

    while dunp_num > 0:
        box_lst[-1] -= 1
        box_lst[0] += 1

        box_lst.sort()
        
        dunp_num -= 1
    
    print(f'#{tc} {box_lst[-1] - box_lst[0]}')