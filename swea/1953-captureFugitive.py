'''
이건 뭐 샤갈 어케하누


'''

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    print(f'#{tc} {result}')