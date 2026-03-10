'''
[초기 생각 및 로직 정리]
집의 수 = num

K**2 + (K-1)**2 <= M * num 을 항상 만족해야함
그리고 위 조건을 만족하는 가장 큰 num을 출력

K = 1 부터 차례대로
위치를 옮겨 가면서 탐색

## 의문점 1. 1(집)이 많은 곳을 어떻게 탐색하는가?
1이 많은 곳을 탐색한다는 것은 각 1 위치에서 delta로 탐색을 하든가 해서 인근의 1의 위치를 탐색한다는건데
사실상 이렇게 하기는 어려움
> 1을 시작점으로 하고, area에서 1의 위치를 탐색
> 찾은 1의 위치를 중심으로 홈 방법 서비스의 영역을 K = 1 ~ K = N 까지 늘리면서 다 조회해보나?
> K = N이면 전체 area가 꽉 참. 단, N이 홀수일 때만.

## 의문점 2. 범위 내의 집의 개수를 어떻게 셀 것인가?
마름모 형태의 범위를 순회하는 방법이 필요함
> 중심을 기준으로 depth = K-1 까지만 delta 탐색하기 > BFS?
> 그럼 BFS 인자로 K랑 위치 좌표만 주면 될 듯
> 그래서 범위 내에 있는 집의 수 num 출력

## 의문점 3. 완탐을 하면 시간초과가 발생할텐데, 어떻게 시간을 줄일 것인가?
일단 박고 시간초과나면 gemini
> 어느 K까지 해보고 그 뒤는 확인해볼 필요없어 라는 수학적 확신이 필요

'''
from collections import deque

def bfs(k, row, column):
    visited = [[False]*N for _ in range(N)]
    queue = deque([(row, column)])
    visited[row][column] = True

    temp_num = 1 if area[row][column] == 1 else 0

    if k == 1:
        return temp_num

    depth = 1

    while queue:
        length = len(queue)

        for _ in range(length):
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

                        if area[nr][nc] == 1:
                            temp_num += 1

        depth += 1

        if depth == k:
            break

    return temp_num

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    total_home_num = float('-inf')

    for r in range(N):
        for c in range(N):
            for k in range(1, N+2):
                home_num = bfs(k, r, c)

                if (k**2 + (k-1)**2) <= M * home_num:
                    total_home_num = max(home_num, total_home_num)

    print(f'#{tc} {total_home_num}')