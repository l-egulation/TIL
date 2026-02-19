def dfs(node):
    pass

for tc in range(1, 11):
    maze = [list(map(int, input().split())) for _ in range(16)]

    start = (1, 1)
    end = (13, 13)

    visited = [[False]*16 for _ in range(16)]
