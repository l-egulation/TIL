n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 0

for r in range(n):
    for c in range(n):
        count = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] == 1:
                    count += 1
        
        if count >= 3:
            answer += 1

print(answer)