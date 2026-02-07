T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    a_idx = 0 # 리스트 A를 가리키는 포인터
    b_idx = 0 # 리스트 B를 가리키는 포인터

    # A와 B의 끝에 도달할 때까지 반복
    while a_idx < N and b_idx < M:
        # 두 리스트의 값이 같다면, B의 다음 글자를 찾으러 갑니다.
        if A[a_idx] == B[b_idx]:
            b_idx += 1
        
        # A는 항상 한 칸씩 앞으로 전진합니다.
        a_idx += 1

    # 결과 판단: B의 포인터가 B의 끝(M)에 도달했다면 모두 순서대로 찾은 것입니다.
    if b_idx == M:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')