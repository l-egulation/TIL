T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    '''
    영역을 순회하면서 1을 만나면 count +1 
    > 근데 가다가 0을 만나면 count = 0, 0으로 초기화
    >> 단어가 들어갈 자리가 못되므로 0으로 초기화하고, 검은색 지나서 다음부터 다시 셀 수 있도록 설계
    > count = K 가 되면, answer +1
    > count > K 가 되면, answer -1하고 count도 0으로 초기화
    >> 글자수 넘은 것이니 들어갈 자리가 아님. 그래서 정답으로 체크한거 -1하고, count도 0으로 초기화해서 다시 계산

    가로 세로 따로니까, 행 순회 열순회 따로 해야겠음
    '''

    answer = 0

    # 행 순회
    for r in range(N):
        # 한 행 돌때마다 count는 0으로 초기화
        # 그래야 각 가로마다 단어가 들어갈 길이를 제대로 확인함
        count = 0
        for c in range(N):
            # 놓을 수 있는 자리면 count +1
            if area[r][c] == 1:
                count += 1
                # 근데 count = K면 정답 수 +1
                if count == K:
                    answer += 1
                # 그러다가 count > K면 정답 수 -1하고 count도 초기화
                elif count > K:
                    count = 0
                    answer -= 1
            # 세다가 0(검은색)을 만나면 count 초기화
            elif area[r][c] == 0:
                count = 0
    
    # 열 순회
    # > 행 순회와 아래 내용 동일
    for c in range(N):
        count = 0
        for r in range(N):
            if area[r][c] == 1:
                count += 1
                if count == K:
                    answer += 1
                elif count > K:
                    count = 0
                    answer -= 1
            elif area[r][c] == 0:
                count = 0
    
    print(f'#{tc} {answer}')