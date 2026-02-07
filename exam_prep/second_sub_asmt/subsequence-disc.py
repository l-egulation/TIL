T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 각 수열의 현재 인덱스 초기 설정
    idx_a = idx_b = 0

    # 몇 번이나 반복해야 할지 모르므로 while문으로 반복
    # 종료 조건은 A나 B의 현재 인덱스가 끝에 다다르면 종료
    while idx_a < N and idx_b < M:
        # 만약 A와 B의 요소가 같다면 B의 현재 인덱스 += 1
        # > 다음 요소가 같은 지 확인하기 위함
        if A[idx_a] == B[idx_b]:
            idx_b += 1
        
        # 원소들의 상대적 순서는 유지 되야하므로 A의 인덱스는 계속해서 증가
        idx_a += 1

        '''
        if문의 위치가 중요한데, if문이 무조건 idx_a += 1 보다 위에 있어야함
        > A 수열의 마지막 요소와 B 수열의 마지막 요소가 같을 수도 있음
        > if문이 idx_a += 1 보다 아래에 있으면 반복과 동시에 A의 인덱스가 증가
        > 그러면서 서로의 마지막 요소가 같아서 if문에서 검증을 하고 idx_b += 1를 해야 idx_b == M이 되서 마지막에 YES가 출력이되는데
        > if문으로 검증하기 전에 idx_a가 늘어나서 종료조건이 충족이 되서 마지막 요소를 확인하지 못하고 종료됨
        '''
    
    # B의 인덱스가 M과 같다면 모두 찾은 것
    # idx_b는 인덱스이므로 B의 길이인 M과 같아질 수 없음
    # > 위의 조건문에서 같은 요소를 찾으면 idx_b += 1인데 마지막 요소를 찾으면 +1이 되면서 idx_b가 B의 길이인 M과 같아짐
    # > 그렇게 된다면 모두 다 찾은 것이니 YES 출력
    if idx_b == M:
        print(f'#{tc} YES')
    else:
        print(f'{tc} NO')