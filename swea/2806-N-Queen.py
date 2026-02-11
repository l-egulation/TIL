'''
Queen을 놓은 자리를 기억해야 함
> 방문체크로
> 체스판이 2차원이니까 방문도 2차원으로
> 행과 열을 기억

visited의 인덱스는 해당 행 번호로

한 행에 하나씩만 데이터가 들어감 > 한 행에 퀸 하나씩이라서
> 그래서 1차원 리스트로 충분함

모든 정점이 아닌 모든 경로 확인 문제
'''


def n_queen(r):
    global answer
    
    if r == N:
        answer += 1
        return
    
    for c in range(N):
        if c in visited:
            continue
        
        for test_r in range(r):
            if r-test_r == abs(c-visited[test_r]):
                break
        else:
            visited[r] = c
            n_queen(r+1)
            visited[r] = -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0

    visited = [-1]*N

    n_queen(0)

    print(f'#{tc} {answer}')