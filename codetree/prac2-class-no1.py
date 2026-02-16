import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
K = int(data[1])
orders = data[2]

forbidden = set()
idx = 3
for _ in range(K):
    fx, fy = int(data[idx]), int(data[idx+1])
    forbidden.add((fx, fy))
    idx += 2

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

dir = {
    'W' : 0,
    'A' : 1,
    'S' : 2,
    'D' : 3
}

r, c = 0, 0

for order in orders:
    m = dir[order]

    nr = r + dr[m]
    nc = c + dc[m]

    if nr < 0 or nr > 30000 or nc < 0 or nc > 30000:
        continue

    if (fx, fy) in forbidden:
        continue

    r = nr
    c = nc

print(nr, nc)