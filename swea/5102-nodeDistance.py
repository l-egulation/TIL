from collections import deque

def bfs():

    while queue:
        global depth
        size = len(queue)

        for _ in range(size):
            curr = queue.popleft()
            if curr == G:
                return depth

            for next_node in links[curr]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

        depth += 1
    
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    links = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        links[u].append(v)
        links[v].append(u)

    S, G = map(int, input().split())

    visited = [False] * (V+1)

    queue = deque([S])
    visited[S] = True
    depth = 0

    result = bfs()
    print(f'#{tc} {result}')