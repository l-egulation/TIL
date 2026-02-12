'''
한 행에 숫자 하나씩만 골라야함
but, 한 열에도 하나씩 고름
> 2차원 리스트에서 리스트 하나 당 값하나만 들어감 
>> 1차원 리스트로 visited해도 충분함
>> 갔다온 열(c)는 True 처리
>> 좀 헷갈리는 개념이긴 한데 한 번 이해하면 나중에 쓰기 쉬움

-------------
**2차원 리스트(matrix)에서 값을 하나씩만 고른다면 1차원 리스트로 visited가 가능한 이유**
위에서 언급한 것처럼 원래 같으면 2차원 리스트로 visited를 구현했을거임
> 왜? matrix가 2차원 리스트니까. 각 좌표마다 visited를 확인해야하니까

But, 그 2차원 리스트안의 여러 리스트 중 각 리스트에 하나씩만 값이 들어간다면?(or 값이 하나씩만 다르다면?)
사실 나머지는 다 빈칸이고 하나만 값이 있기때문에 공간 낭비임

그렇다면 1차원 리스트의 index가 2차원 리스트의 행 번호가 된다면?
> 각 인덱스에 하나의 값 -> 그 값이 열 번호가 되면 1차원 리스트로 visited처리가 가능함
>> 역시 말로는 어려우니 직접 확인

matrix = [
    [2, 1, 2]    < 0번 row(행)
    [5, 8, 5]    < 1번 row
    [7, 2, 2]    < 2번 row
     0  1  2     << 순서대로 col(열) 번호
]
             0     1      2     < visited index 번호
visited = [True, False, False]
> 보는 것처럼 visited는 0번 index부터 2번까지 있음
> 느꼈을지 모르겠지만 위의 matrix 바로 밑에 visited를 가져가면 col 번호랑 위치가 일치함
>> 그렇게 visited의 index번호를 col 번호라고 생각
>> 지금 visited[0] = True 임 -> 이는 곧 0번 col에는 이미 방문했다는 뜻

그래서 아래 search 함수 정의문 안에 
for c in range(N):
    if not visited[c]:
        visited[c] = True
라고 되있는데, 0 ~ N-1까지의 c 중에 순서대로 c = 0이라고 친다면
만약 0번 col을 방문하지 않았다면(조건문을 번역한 것, not을 해제한다면 if visited[c] == False: 임)
visited[0] (0번 col에 해당하는 False)를 True로 바꿔라! > 즉, 0번 col 갈꺼니까 방문처리해라

그래서 실제로 True처리하고 밑에서 
search(row+1, current_sum + matrix[row][c])
해서 row+1해서 다음 행으로 넘어가면서 0번 col은 True니까 if 조건문에 걸리면서 다음 c=1로 넘어가는 것
-------------

순열처럼 뽑은 숫자가 3개가 되면 다시 뒤로 돌아가서 다음 for문 순서로 넘어감(c -> c+1)
> 물론 visited[c] = False하고 넘어감
>> 그래야 다음 차례에 다른 걸 쓸 수 있음

그리고 2개까지 sum한걸 구했는데 이미 전에 구했던 3개의 합보다 더 크면 3번째 숫자까지 더할 필요가 없음
> 그래서 current_sum이 min_ans보다 크면 다시 return
>> 백트레킹 구현으로 좀 더 쾌적하게 함
'''
# 매개변수로 row와 current_sum을 받는 이유 :
# row는 계속 +1 하면서 재귀를 하면서 다음 행으로 넘어가는 구조
# current_sum도 뽑은 숫자를 계속 current_sum에 += 하면서 합산하는 구조
def search(row, current_sum):
    global min_ans
    
    # 현재까지 더한 값이 이미 찾은 최솟값보다 크면 더 해볼 필요가 없음
    # > return해서 백트레킹
    # > 이미 최솟값보다 크니까 돌아가서 다른 숫자 선택해와
    if current_sum >= min_ans:
        return

    # row = N 이라는 건, 0 ~ N-1까지 다 골랐다는 뜻
    # > row는 index라 0 ~ N-1 까지 밖에 없는데, 마지막 숫자를 고르고 row+1을 하기때문에 row = N까지 갈 수 있음
    # >> 그래서 row = N 이면 min_ans중에 가장 작은 값,
    # 즉, 최솟값을 갱신하고(원래 최솟값이 더 작으면 원래 값으로 적용됨) return
    # min_ans(변수명) = min(A, B)
    # > min(A, B) : A와 B 둘 중에 작은 값을 변수에 할당해라
    if row == N:
        min_ans = min(min_ans, current_sum)
        return
    
    # 0 ~ N-1 까지의 열을 순회
    for c in range(N):
        # 만약 c번 열을 선택한적이 없다면,
        # visited[c]가 False라면,
        if not visited[c]:
            # 이번에 선택한 c(col, 열 번호)를 True처리하고 > 방문했다하고
            visited[c] = True
            # row + 1해서 다음 행으로 넘어가면서, matrix의 현재 값을 current_sum에 누적합해라
            search(row+1, current_sum + matrix[row][c])
            # 그리고 N개의 숫자를 다 합산해서 여기로 돌아오면 c번 열을 False처리해서
            # 다시 고를 수 있도록 하는것
            # 안하면 영원히 c번 열에서 숫자 못고름
            visited[c] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 위에서 말한 것처럼 1차원 visited
    visited = [False] * N
    # visited = [-1] * N
    
    # 초기 최솟값은 가장 큰 값으로 할당
    min_ans = float('inf')

    # row = 0, current_sum = 0 으로 처음부터 시작
    search(0, 0)

    print(f'#{tc} {min_ans}')