T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    # memo[i]가 1이면 i에서 i+1로 갈 수 있다는 뜻
    memo = [0] * (N*N + 1)

    for r in range(N):
        for c in range(N):
            curr_value = area[r][c]

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N:
                    if area[nr][nc] == curr_value + 1:
                        memo[curr_value] = 1

                        # 정확히 1 더 큰 수는 area에 단 하나
                        # 그래서 하나만 찾으면 바로 break
                        break

    max_dist = 0
    start_node = 0

    # 현재 연속된 방의 개수
    curr_dist = 0

    # N*N부터 1까지 거꾸로 내려감
    for i in range(N*N, 0, -1):
        if memo[i]:
            # 연결되어 있다면 +1
            curr_dist += 1
        else:
            # 연결이 끊겼다면 다시 1부터 시작 (자기자신)
            curr_dist = 1

        # 매 순간 최댓값을 갱신
        # 역순으로 내려가고 있기 때문에, >= 를 쓰면
        # 거리가 같을 때 더 작은 방 번호(i)가 자동으로 저장
        if curr_dist >= max_dist:
            max_dist = curr_dist
            start_node = i

    print(f'#{tc} {start_node} {max_dist}')