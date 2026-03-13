def dfs(idx, curr_height):
    global answer

    # [가지치기] 이미 현재 합산이 최솟값을 넘어섰다면, 더 할 필요 X
    if curr_height - B >= answer:
        return

    # [조건] 선반 높이 B를 넘었다면 최솟값 갱신 후 return
    # > 최솟값이 목적이라 넘은 순간 뒤에 더 더할 필요 X
    if curr_height >= B:
        answer = min(answer, curr_height - B)
        return

    # [기저조건] 모든 점원을 다 확인을 했는데 B를 못넘은 경우
    if idx == N:
        return

    # 1. 현재 점원을 포함하는 경우
    dfs(idx + 1, curr_height + numbers[idx])

    # 2. 현재 점원을 미포함하는 경우
    dfs(idx + 1, curr_height)

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    numbers = list(map(int, input().split()))

    answer = float('inf')

    dfs(0, 0)

    print(f'#{tc} {answer}')