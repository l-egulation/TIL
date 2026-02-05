T = int(input())

for tc in range(1, T+1):
    N = int(input())

    snail_lst = [[0] * N for _ in range(N)]

    num_lst = []
    for num in range(1, N*N+1):
        num_lst.append(num)
    
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
    '''

    rotate_tim = 0

    for r in range(N):
        for c in range(N):
            snail_lst[r][c] = num_lst[rotate_tim]
            rotate_tim += 1
            if rotate_tim == N:
                r, c = c, r
                break
            
            print(snail_lst[r][c], end=' ')
            # for num in range(1, N*N+1):
            #     snail_lst[r][c] = num
            #     print(snail_lst[r][c])
            #     if r == N and c == N:
            #         breaks