'''
부술 수 있는 횟수가 늘어남에 따라 visited와 조건문이 바뀌어야함
> 근데 뭐 조건문을 for문으로 돌릴 수도 없고...
>> 돌리면 되겠는데?

------------------------------------------------------------

처음에
for k in range(0, K):
    if broken == k:
        if not visited[nr][nc][k+1]:
            visited[nr][nc][k+1] = 1
            queue.append((nr, nc, k+1))

이렇게 했는데 비효율적이라고 함
> K가 최대 10인데, 10번의 for문을 돌면서 if문에 단 한 번 걸림
> 시간적 낭비
>> 그래서 if broken < K: 를 하면 그 딱 한번만 걸림
>> 어짜피 K는 벽을 부술 수 있는 횟수라서 K보다 작을때만 작동하면 됨
>> 그렇게 층을 올라가는 느낌?

그래서 지금의 if broken < K: 로 수정함

------------------------------------------------------------

시간초과나서 다시 수정함

1. visited 수정
> 단순히 '방문했다(True/False)'가 아니라 '최소 몇 번 부수고 왔나'를 기록함
> BFS는 거리순으로 움직이므로, 같은 거리에 도달했을 때 벽을 '덜' 부순 쪽이 무조건 남은 길에서 유리함
>> 잠재력이 높음
> 따라서 '예전 기록보다 더 적게 부수고 도착'했을 때만 큐에 넣어서 탐색 범위를 줄임

2. 덧셈 활용
> if area == 0, elif area == 1 등의 조건 분기문을 수식 하나로 대체
> 조건 판단(if)보다 산술 연산(+)이 훨씬 빠르기 때문에 변경

'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    # 초기값을 K+1로 해서 아무도 안 갔음을 표현
    # > K번까지 부술 수 있는데 K+1을 적어서 한 번도 도달한 적 없음을 표현한 것
    # 단순히 방문체크가 아니라, 해당 칸에 가장 벽을 적게 부쉈던 기록을 저장
    visited = [[K+1] * M for _ in range(N)]
    # r, c, broken, dist
    # > 현재 행 좌표, 현재 열 좌표, 현재 벽 부순 횟수, 현재까지의 거리
    queue = deque([(0, 0, 0, 1)])
    # 시작점 벽 0번 부숨 표현
    visited[0][0] = 0

    while queue:
        for _ in range(len(queue)):
            r, c, broken, dist = queue.popleft()

            # 목적지 도달하면 함수 종료 후 이동거리 반환
            if r == N-1 and c == M-1:
                return dist

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < M:
                    # 다음 칸이 벽이면 +1, 길이면 +0
                    # > if-else로 안나눠도 부순 횟수가 자동으로 계산됨
                    next_broken = broken + area[nr][nc]

                    # 1. 벽을 횟수제한 이내로 부쉈는가?
                    # 2. 전에 이 칸을 방문했던 사람보다 더 적게 벽을 부쉈는가?
                    if next_broken <= K and visited[nr][nc] > next_broken:
                        # 벽을 덜 부쉈으니까 더 적은 벽 부수기 횟수 기록하고 큐에 삽입
                        visited[nr][nc] = next_broken
                        queue.append((nr, nc, next_broken, dist + 1))

    # 모든 경로를 뒤졌는데도 목적지 도달 못하면 -1
    return -1

N, M, K = map(int, input().split())
area = [list(map(int, list(input().strip()))) for _ in range(N)]

print(bfs())