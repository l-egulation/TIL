'''
단순 BFS는 아님
벽을 부수고 이동해야함
> 가존의 1(벽)을 0(아동할 수 있는 곳)으로 바꾸고 이동하는 방법이 필요
> 추가로 벽을 부수지 않아도 최단거리가 있다면 그 거리를 구해야함

visited를 2개를 사용해야된다고 함

다차원의 visited를 처음엔 이해하기 힘들었음
근데 아파트의 층으로 생각하고 벽을 부수면 다음 층으로 이동해서 진행하는 느낌으로 이해함
visited도 한 좌표에 [False, False] 이렇게 2개로 해서 벽을 부수면 1번 인덱스로만 기록해서 쭉 가는느낌

visited의 두 차원이 투영되서 비교하고 더 이상 이 경로를 진행할 가치의 여부를 어떻게 판단하는지 잘 모르겠음
> BFS가 진행되면서 4방향으로 탐색하면서 계속 좌표들을 담음
> 그 중에는 0인 좌표도 있고 1인 좌표도 있음
> 그러면서 1을 만나면 벽을 부수면서 진행하고 아니면 계속 안부수고 진행
> 결국에는 도착지에 가장 먼저 도착하는 경로가 생김
>> 그것이 최단거리
>> 결국 알고리즘이 판단하기보다 그냥 수 없이 많은 멀티버스에서 가장 빨리 도착한 시간선이 정답이 되는 것
>> 글로 적으니 좀 이상하긴 한데 어쨌든 이해함
'''

from collections import deque
import sys

def bfs_break_move():
    # 입력 처리
    input = sys.stdin.read().split()
    if not input: return
    
    N = int(input[0])
    M = int(input[1])
    board = [list(map(int, list(row))) for row in input[2:]]

    # 3차원 방문 배열: visited[row][col][wall_broken]
    # visited[r][c][0]: 벽을 안 부수고 해당 좌표에 도달한 적이 있는지
    # visited[r][c][1]: 벽을 부수고 해당 좌표에 도달한 적이 있는지
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

    # 큐 데이터 구성: (row, col, broken_status)
    # broken_status: 0(안 부숨), 1(이미 부숨)
    q = deque([(0, 0, 0)])
    visited[0][0][0] = True
    
    depth = 1 # 시작 칸을 포함하므로 1부터 시작

    while q:
        # 큐의 현재 길이만큼 반복하여 같은 거리(depth)에 있는 노드들만 처리
        current_layer_size = len(q)
        for _ in range(current_layer_size):
            r, c, broken = q.popleft()

            # 목표 지점 도착 시 현재까지의 거리 반환
            if r == N - 1 and c == M - 1:
                return depth

            # 4방향 탐색
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                # 지도 범위 안인지 확인
                if 0 <= nr < N and 0 <= nc < M:
                    # sit. 1: 다음 칸이 길(0)인 경우
                    if board[nr][nc] == 0:
                        # 현재 내 상태(부쉈는지 여부)에 맞는 방문 기록 확인
                        if not visited[nr][nc][broken]:
                            visited[nr][nc][broken] = True
                            q.append((nr, nc, broken))

                    # sit. 2: 다음 칸이 벽(1)인 경우
                    elif board[nr][nc] == 1:
                        # 아직 벽을 부순 적이 없다면(broken == 0) 부술 수 있음
                        if broken == 0:
                            # 벽을 부수고 이동한 세계(index 1)에 방문 기록이 없다면 이동
                            if not visited[nr][nc][1]:
                                visited[nr][nc][1] = True
                                q.append((nr, nc, 1)) # 이제부터는 '이미 부순 상태(1)'로 진행

        depth += 1 # 한 레이어 탐색이 끝나면 거리를 1 증가

    return -1 # 끝내 도착하지 못한 경우

print(bfs_break_move())