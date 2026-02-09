T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    # 삼각형 모양으로 2차원 리스트를 만듦
    triangle = [[1] * (i+1) for i in range(N)]

    # 0번째, 1번째, 리스트는 반복문을 돌면서 계산할 필요가 없어서 범위에서 제외
    # > 0, 1번째는 이미 만들어져 있기 때문
    # 2번째 리스트부터 선택
    for i in range(2, N):
        # 첫 번째 요소와 마지막 요소는 1로 고정이므로 범위에서 제외
        for j in range(1, len(triangle[i])-1):
            # 중간 값들만 파스칼의 삼각형의 원리로
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    print(f'#{tc}')
    # 하나씩 출력
    for i in range(N):
        print(*triangle[i])