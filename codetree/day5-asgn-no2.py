import sys
input = sys.stdin.readline

commands = input().strip()

x, y = 0, 0
curr_dir = 0

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0

for cmd in commands:
    time += 1

    if cmd == 'L':
        curr_dir = (curr_dir - 1) % 4

    elif cmd == 'R':
        curr_dir = (curr_dir + 1) % 4

    elif cmd == 'F':
        x += dx[curr_dir]
        y += dy[curr_dir]
        
        if x == 0 and y == 0:
            print(time)
            exit()

print(-1)