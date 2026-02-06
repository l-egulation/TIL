for tc in range(1, 11):
    N = int(input())
    area = [list(input()) for _ in range(8)]

    '''
    N이 짝수 or 홀수에 따라 회문을 찾는게 달라짐

    N이 짝수라면 (N%2 = 0)
    앞 뒤로 N//2만큼 자르고 [0:N//2] = [:N//2-1:-1] 가 되야 회문
    N이 홀수라면 (N%2 = 1)
    앞 뒤로 N//2번 인덱스를 기준으로 [0:N//2] = [:N//2:-1] 가 되야 회문
    > 근데 홀수일 때, 가운데를 포함해서 반전시켜서 비교해도 되니까 조건문을 한 번에 합칠 수 있음
    > lst[:N//2] == lst[:(N-1)//2:-1]
    > 홀수일 때는 중간거 포함해서 비교, 짝수일땐 앞 뒤만 비교.

    이제 8x8 영역에서 회문을 찾아야함
    가로 회문은 for 문 돌면서 찾는다고 친다면,
    세로 회문은?
    > 걍 가로 세로 둘 다 돌면서 찾아야될 듯
    '''
    num_palin = 0

    for r in range(8):
        for c in range(8-N+1):
            h_lst = area[r][c:c+N]
            if h_lst[:N//2] == h_lst[:(N-1)//2:-1]:
                num_palin += 1
    
    for r in range(8-N+1):
        for c in range(8):
            v_lst = [area[r+i][c] for i in range(N)]
            if v_lst[:N//2] == v_lst[:(N-1)//2:-1]:
                num_palin += 1

    print(f'#{tc} {num_palin}')