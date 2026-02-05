T = int(input())

for tc in range(1, T+1):
    N = int(input())
    color_lst = [list(map(int, input().split())) for _ in range(N)]

    # 10*10 영역 생성
    area =[[0]*10 for _ in range(10)]

    # color = 1 > red
    # color = 2 > blue
    # color = 3 > purple

    for colors in color_lst:
        # 색과 색 위치 정보가 담긴 리스트를 순회하면서 꼭짓점 위치 할당
        r1, c1, r2, c2, color = colors

        # 마지막 요소가 색이므로 색을 구분해서 해당 영역에 1 or 2를 더함
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                area[r][c] += color
        
    # 영역 내의 보라색(3)이 몇 개인지 확인
    answer = sum(r.count(3) for r in area)

    print(f'#{tc} {answer}')