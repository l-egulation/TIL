# 이진 검색 정의
def binary_search(num, key):
    #인덱스가 아니라 주어진 페이지 수로 하기때문에 0, num-1 이 아닌 1, num
    start, end = 1, num
    search_time = 0
    
    while start <= end:
        # while문 반복될 때마다 찾는 횟수 +1
        search_time += 1
        mid = int((start + end)//2)
        if mid == key:
            return search_time
        # 찾는 값보다 크면 끝 값을 중간값으로 바꿔서 왼쪽 구간 선택
        elif mid > key:
            end = mid
        # 찾는 값보다 작으면 시작 값을 중간값으로 바꿔서 오른쪽 구간 선택
        else:
            start = mid
    return search_time

T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    time_A = binary_search(N, A)
    time_B = binary_search(N, B)

    if time_A > time_B:
        print(f'#{tc} B')
    elif time_A < time_B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')