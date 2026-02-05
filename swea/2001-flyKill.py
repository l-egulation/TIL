T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    '''
    그래서 M범위만큼 리스트 내부 슬라이싱해서 sum때리기
    행 열 각각 N-M+1번 해야함 => N-M+1 * N-M+1
    '''

    total_sum_lst = []

    for r in range(0, N-M+1):
        for c in range(0, N-M+1):
            total_sum = 0
            for m in range(0, M):
                total_sum += sum(arr[r+m][c:c+M])
            total_sum_lst.append(total_sum)
    
    ans = max(total_sum_lst)

    print(f'#{tc} {ans}')