T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    temp_lst = []

    for i in range(len(B)-1):
        if B[i] in A:
            if A.index(B[i]) > A.index(B[i+1]):
                continue
            char = B[i]
            temp_lst.append(char)
            j = A.index(B[i])
            A = A[j+1:]
        elif B[i] not in A:
            continue
    
    print(temp_lst)

    if temp_lst == B:
        print(f'#{tc} YES')
    elif temp_lst != B:
        print(f'#{tc} NO')