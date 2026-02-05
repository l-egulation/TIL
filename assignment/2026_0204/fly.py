T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # dr = [-1, 0, 1, 0]
    # dc = [0, 1, 0, 1]
    '''
    dr, dc를 같은 인덱스끼리 한 쌍으로 봤을 때, 0번부터 차례대로 상, 하, 좌, 우
    근데 델타로 하면 M < 3 되면 진짜 개골때릴듯
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