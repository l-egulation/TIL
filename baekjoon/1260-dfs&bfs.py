import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

#DFS
def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')

    for next_node in graph[n]:
        if not visited_dfs[next_node]:
            dfs(next_node)

visited_dfs = [False] * (N+1)
dfs(V)
print()

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        n = queue.popleft()
        print(n, end=' ')

        for next_node in graph[n]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)

visited_bfs = [False] * (N+1)
bfs(V)