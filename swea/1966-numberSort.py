T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    # 선택 정렬

    # 어짜피 최대값은 맨 뒤로 가니까 끝까지 할 필요없음
    for i in range(N-1):
        # 일단은 현재 인덱스를 최소값 인덱스로 함
        min_idx = i
        # 맨 앞을 최소값 인덱스로 했으니까 그 다음 순서인 i+1부터 검사는 끝까지 해야되니까 N까지
        for j in range(i+1, N):
            # 현재 값이 최솟값보다 작으면 지금 인덱스를 최소값 인덱스에 할당
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
        # 그리고 최솟값과 방금 검사한 값의 위치를 변경
        num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

    print(f'#{tc}', *num_lst)