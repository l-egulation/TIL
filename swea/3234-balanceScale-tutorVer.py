# count : 뽑은 개수
# visited : 현재 뽑아놓은 상태
# left / right : 왼쪽과 오른쪽의 무게
# > 오른쪽이 무거워지면 안되니까 체크하기 위함
def dfs(count, visited, left, right):

    if count == N:
        return 1

    # 현재 방문 상태에서 left 무게를 이미 셌다면?
    if dp[visited].get(left):
        return dp[visited][left]

    temp = 0

    for i in range(N):
        # i번째 무게추를 골랐다면 건너뛰기
        if visited & (i << i):
            continue

        dfs(count+1, visited | (1 << i), left + weights[i], right)

        if left >= right + weights[i]:
            temp += dfs(count+1, visited | (1 << i), left, right + weights[i])

    # 현재 visited 상태에서 left 무게일 때의 경우의 수를 반환
    dp[visited][left] = temp
    return dp[visited][left]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))

    dp = [{} for _ in range(2**N)]
    '''
    비트마스킹 활용

    원래 기존에는 dp[key] = value 였음
    지금은 왼 오에 따라 달라짐
    3개가 필요
    1. 뽑은 것, 2. left, 3. right
    > 1, 2만 있으면 됨 > 뽑은거랑 left알면 right는 자동으로 앎

    dp[key][left] = value > 2차원

    일단 key만큼 배열이 있어야됨
    2^0, 2^1, ... , 2^(N-1) > 2^(N-1) - 1 만큼 있어야함
    key는 1씩 연속이지만, left는 공간 낭비가 심함

    그래서 left는 dict으로 넣음
    dp[방문상태][왼쪽 무게]
    '''

    answer = dfs(0, 0, 0, 0)

    print(f'#{tc} {answer}')