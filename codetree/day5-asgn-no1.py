import sys

data = sys.stdin.read().split()

N = int(data[0])

idx = 1
moves = []

for _ in range(N):
    char = data[idx]
    num = int(data[idx+1])
    moves.append((char, num))
    idx += 2

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

dir = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3
}

r, c = 0, 0
time = 0

for char, num in moves:
    for _ in range(num):
        r += dr[dir[char]]
        c += dc[dir[char]]
        time += 1

        if r == 0 and c == 0:
            print(time)
            exit()

print(-1)