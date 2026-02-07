def selection_sort(a, N) :
    for i in range(N-1) :                   # 정렬 구간의 시작 인덱스
        min_idx = i                         # 첫 원소를 최솟값으로 가정
        for j in range(i+1, N) :
            if a[min_idx] > a[j] :          # 최솟값의 인덱스 갱신
                min_idx = j
        a[i],a[min_idx]= a[min_idx],a[i]    # 구간 최솟값을 구간 맨 앞으로