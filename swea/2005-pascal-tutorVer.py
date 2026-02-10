T = int(input())

for tc in range(1, T+1):
    # 출력할 삼각형의 층수 N
    N = int(input())
    
    # '직전 줄'의 데이터를 저장할 리스트입니다. > 일종의 메모지
    # 처음에는 아무것도 없으니 빈 리스트로 시작
    before_row = [] 

    # 테스트 케이스 번호를 먼저 출력
    print(f'#{tc}')

    # 첫 번째 줄부터 N번째 줄까지 한 줄씩 만듭니다. > i는 현재 층수
    for i in range(1, N+1): 
        # '현재 줄'의 데이터를 담을 리스트를 매번 새로 제작
        current_row = [] 

        # 현재 줄(i층)에는 i개의 숫자가 들어감 > j는 칸의 번호
        for j in range(i):
            # 양 끝(첫 번째 칸 j=0 또는 마지막 칸 j=i-1)은 항상 1
            if j == 0 or j == i-1:
                # 현재 줄 리스트에 1 추가
                current_row.append(1)
                # 화면에 1 출력 (줄바꿈 없이 공백 한 칸)
                print(1, end=" ")

            # DP 점화식 > 양 끝이 아닌 가운데 숫자들은 계산이 필요
            else:
                # 직전 줄(before_row)의 같은 위치(j)와 그 왼쪽(j-1)을 더함
                # 이 부분이 바로 "이미 계산된 값을 재사용"하는 메모이제이션의 핵심
                value = before_row[j] + before_row[j-1]
                
                # 계산된 값을 현재 줄 리스트에 저장
                current_row.append(value)
                # 계산된 값을 화면에 출력
                print(value, end=" ")
        
        # 한 줄의 숫자 출력이 모두 끝나면 줄바꿈을 해줌
        print()

        # **다음 층을 계산하기 위해, 지금 만든 '현재 줄'을 '직전 줄'로 업데이트**
        # > 이렇게 하면 다음 i 루프에서 이 정보를 보고 다음 줄을 만들 수 있음
        before_row = current_row