'''
5x5 2차 배열에 25개의 숫자를 저장
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
예를 들어 아래 그림에서 7의 이웃한 값은 2, 6, 8, 12 이며 차의 절대값의 합은 12 이다.
.. 2 ..
6  7  8 
.. 12 ..
25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
벽에 있는 요소는 이웃한 요소가 없을 수 있음에 주의하시오.
ex. [0][0]은 이웃한 요소가 2개이다.
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    '''
    NxN 전체 다 순화하면서 상 하 좌 우 값과의 차의 절대값의 합을 구해햐함
    arr의 범위에 벗어나지않게 해야함
    > 조건문으로 범위 설정하기 (i < 0, i > N)
    끝 라인은 어떡하지?
    > 범위에 벗어나면 벗어나는 인덱스?는 제외하고 주위 요소와의 차 계산
    > 대충 현재 합 변수에 += 해서 리스트에 append하고 리스트합 구해서 출력
    [r-1][c], [r+1][c], [r][c-1], [r][c+1]
    > 범위가 벗어나서 Index 에러가 안나도록 해야함
    > 그걸 조건문으로 범위 벗어나면 계산하지 않도록 해서 에러 방지하는게 되나?
    '''
    
    sum_lst = []

    for r in range(N):
        for c in range(N):
            current_sum = 0
            if r-1 >= 0:
                current_sum += abs(arr[r][c] - arr[r-1][c])
            if r+1 < N:
                current_sum += abs(arr[r][c] - arr[r+1][c])
            if c-1 >= 0:
                current_sum += abs(arr[r][c] - arr[r][c-1])
            if c+1 < N:
                current_sum += abs(arr[r][c] - arr[r][c+1])

            sum_lst.append(current_sum)

    result = sum(sum_lst)

    print(f'#{tc} {result}')