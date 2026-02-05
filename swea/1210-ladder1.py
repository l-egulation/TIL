for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    '''
    한 줄씩 넘어가면서 1인 지점을 찾아야함
    1인 지점에서 양 옆에 1이 존재한다면 존재하는 쪽으로 이동
    단, 아래로 이동할 때는 전 줄과 같은 인덱스여야함
    
    근데 위에서 아래로 가면 계산해야할 경우의 수가 너무 많음
    => 도착 지점인 맨 아랫줄 2에서 사다리를 타고 올라가야함

    맨 아랫줄 2에서부터 한 줄씩 올라가면서 1을 탐색(index로는 -1)
    확인할 순서가 있는 듯함
    1. 다음 줄의 같은 index에 1이 있는가?
        - 있다면 다음 조건으로 넘어감 (없을 수는 없음)
        
    2. 같은 index에 있는 1의 양 옆에 1이 또 있는가?(무조건 왼 or 오 둘 중 하나에만 있음)
        - 있다면 1이 있는 쪽으로 이동
        - 없다면 기존의 같은 index의 1 로 이동
    
    무조건 바로 위에는 1이 있고, 그 1의 양 옆에 1이 있을 수도 있고 없을 수도 있음

    for문에서 range 거꾸로 해서 마지막 줄부터 탐색하기

    그냥 idx 1씩 빼고 더하면 dr dc 안써도 됨

    근데 또 올라가다가 왼쪽이나 오른쪽으로 이동하면 자기 위에 1 있을때까지 계속 사다리있는 쪽으로 가야되는데 그때는 저 조건문이 통하나?
    '''

    # 일단 도착 지점을 찾아야함 > 정확히는 도착지점의 idx를 알아야 함
    goal_idx = now_idx = ladder[-1].index(2)
    # 에러 방지로 if 2 in ladder[-1]: \n goal_idx = ladder[-1].index(2) 을 해야하지만 지금은 확실하게 있다는걸 아니까 안함

    for i in range(100-2, -1, -1):
        # 다음 줄의 now_idx 인덱스의 양 옆에 1이 있는가를 확인
        # 있다면 그 쪽으로 이동 > dir을 다른 값으로 바꿔서(좌 = 0 , 우 = 1 > dir = 1 or dir = 1) 이동

        # 만약 왼쪽에 1이 있다면 좌로 이동
        if now_idx > 0 and ladder[i][now_idx-1] == 1:
            # 그 길이 끝날때까지 좌로 이동
            while now_idx > 0 and ladder[i][now_idx-1] == 1:
                now_idx -= 1

        # 만약 오른쪽에 1이 있다면 우로 이동
        elif now_idx < 99 and ladder[i][now_idx+1] == 1:
            # 그 길이 끝날때까지 우로 이동
            while now_idx < 99 and ladder[i][now_idx+1] == 1:
                now_idx += 1

    print(f'#{T} {now_idx}')